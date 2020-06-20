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
        if 'venv' in func_filename:
            return
        if 'python3.8' in func_filename:
            return

        print('func_filename', func_filename)

        if event == 'call':
            docstring = None
            arg_names = code.co_varnames[0:code.co_argcount]
            arg_dict = frame.f_locals
            filename = frame.f_code.co_filename
            # print('CALL ARGS', func_name, arg_dict)
            # get doctstring
            func_details = frame.f_back.f_globals.get(func_name)
            if func_details:
                docstring = func_details.__doc__
            # get function class
            class_name = self.get_class_from_frame(frame)
            # called by?
            caller = frame.f_back
            if caller:
                caller_func = caller.f_code.co_name
                caller_line_no = caller.f_lineno
                caller_filename = caller.f_code.co_filename
                # print('CALLER', caller_func, caller_line_no, caller_filename)

            self.traces[func_name] = dict(
                name=func_name,
                filename=filename,
                caller=caller_func,
                caller_file=caller_filename,
                call_args=arg_names,
                call_number=self.call_number,
                docstring=docstring,
                class_name=class_name,
            )
            self.call_number += 1
            return self

        elif event == 'return':
            # print('RETURN ARGS', func_name, arg)
            call_dict = self.traces.get(func_name, {})
            call_dict.update(
                dict(
                    return_value=arg,
                )
            )
            self.traces[func_name] = call_dict
            return self

    def get_class_from_frame(self, frm):
        args, _, _, value_dict = inspect.getargvalues(frm)
        # we check the first parameter for the frame function is
        # named 'self'
        if len(args) and args[0] == 'self':
            # in that case, 'self' will be referenced in value_dict
            instance = value_dict.get('self', None)
            if instance:
                # return its class
                return getattr(instance, '__class__', None)
        # return None otherwise
        return None
