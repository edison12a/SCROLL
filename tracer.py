
import inspect


class Tracer:
    def __init__(self):
        pass

    def __call__(self, frame, event, arg):
        code = frame.f_code
        func_name = code.co_name
        func_line_no = frame.f_lineno
        func_filename = code.co_filename

        # # Ignore write() calls from printing
        # if func_name == 'write':
        #     return

        # # Ignore calls not in this module
        # if not func_filename.endswith('example.py'):
        # if 'venv' in func_filename:
        #     return

        if event == 'call':
            arg_names = code.co_varnames[0:code.co_argcount]
            arg_dict = frame.f_locals
            print('CALL ARGS', func_name, arg_dict)
            # called by?
            caller = frame.f_back
            if caller:
                caller_func = caller.f_code.co_name
                caller_line_no = caller.f_lineno
                caller_filename = caller.f_code.co_filename
                print('CALLER', caller_func, caller_line_no, caller_filename)
            return self

        elif event == 'return':
            doc = None
            name = code.co_name
            func_details = frame.f_back.f_globals.get(name)
            if func_details:
                doc = func_details.__doc__
            print('RETURN ARGS', func_name, arg)
            # print('__doc__', doc)
            print('class', self.get_class_from_frame(frame))
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
