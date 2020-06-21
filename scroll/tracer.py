import inspect


class Tracer:
    def __init__(self):
        self.traces = {}
        self.call_number = 1

    def __call__(self, frame, event, arg):
        code = frame.f_code
        func_name = code.co_name
        func_line_no = frame.f_lineno
        func_filename = code.co_filename

        # # Ignore write() calls from printing
        if func_name in ('write', '_shutdown'):
            return
        # # Ignore calls not in this module
        if 'venv' in func_filename \
            or func_filename.startswith('<') \
            or func_name.startswith('<') \
            or 'python3.8' in func_filename:
            return

        # everuthing beyond this point gets evaluated
        print(func_filename)

        if event == 'call':
            docstring = None
            arg_names = code.co_varnames[0:code.co_argcount]
            arg_dict = frame.f_locals
            
            # get doctstring
            func_details = frame.f_globals.get(func_name)
            if func_details:
                docstring = func_details.__doc__

            # get function class name and dostring
            class_obj = self.get_class_from_frame(frame)
            if class_obj:
                class_name = class_obj.__name__
            else:
                class_name = ''

            if func_name == '__init__':
                docstring = class_obj.__doc__

            # called by?
            caller = frame.f_back
            if caller:
                caller_func = caller.f_code.co_name
                caller_line_no = caller.f_lineno
                caller_filename = caller.f_code.co_filename
                # caller_class = self.get_class_from_frame(caller)
                # record the call in the caller dict
                if self.traces.get(caller_func):
                    if class_name:
                        key_name = f"{class_name}.{func_name}"
                    else:
                        key_name = func_name
                    callees = self.traces[caller_func]['calls']
                    callees.add(key_name)
                    self.traces[caller_func]['calls'] = callees

            else:
                print(caller, func_name)

            self.traces[func_name] = dict(
                name=func_name,
                filename=func_filename,
                caller=caller_func,
                caller_file=caller_filename,
                call_args=arg_names,
                call_number=self.call_number,
                # docstring=docstring, 
                docstring=type(docstring), #todo 
                class_name=class_name,
                calls=set(),
            )

            self.call_number += 1
            return self

        elif event == 'return':
            # print('RETURN ARGS', func_name, arg)
            call_dict = self.traces.get(func_name, {})
            call_dict.update(
                dict(
                    # return_value=arg,
                    return_value=type(arg), #todo
                )
            )
            self.traces[func_name] = call_dict
            return self

    def get_class_from_frame(self, frm):
        # initialize as None
        class_obj = None
        args, _, _, value_dict = inspect.getargvalues(frm)
        # we check the first parameter for the frame function is
        # named 'self'
        if len(args) and args[0] == 'self':
            # in that case, 'self' will be referenced in value_dict
            instance = value_dict.get('self', '')
            if instance:
                # return its class
                class_obj =  getattr(instance, '__class__', None)
        return class_obj
