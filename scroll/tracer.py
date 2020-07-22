import inspect
import os
from scroll.helpers import OrderedSet

class Tracer:
    def __init__(self):
        self.traces = {}
        self.call_number = 1
        self.cwd = os.getcwd()

    def __call__(self, frame, event, arg):
        code = frame.f_code
        func_name = code.co_name
        func_filename = code.co_filename

        # # Ignore write() calls from printing
        if func_name in ('write', '_shutdown'):
            return
        # # Ignore calls not in this module
        if 'venv' in func_filename \
            or func_filename.startswith('<') \
            or func_name.startswith('<') \
            or 'python' in func_filename:
            return

        # get function class name
        class_name = self.get_class_name(frame)
        key_name = f"{class_name}.{func_name}"

        if event == 'call':
            self.handle_call(frame, key_name, func_name, func_filename, class_name)

        elif event == 'return':
            self.handle_return(arg, key_name)

    def handle_call(self, frame, key_name, func_name, func_filename, class_name):
        code = frame.f_code
        func_name = code.co_name
        func_line_no = frame.f_lineno
        func_filename = code.co_filename

        docstring = None
        arg_names = code.co_varnames[0:code.co_argcount]
        arg_dict = frame.f_locals

        # create a  dict of args and their types
        arg_values = {}
        for name in arg_names:
            if name in arg_dict:
                value = arg_dict[name]
                arg_values[name] = type(value).__name__
                # arg_values[name] = dict(
                #     arg=value,
                #     type=type(value)
                # )

        # get doctstring
        docstring = self.get_docstring(func_name, frame)

        # prevent python object from going into DB
        if not docstring:
            doctstring = 'Un-Documented'

        # called by?
        caller = frame.f_back
        if caller:
            caller_func = caller.f_code.co_name
            caller_line_no = caller.f_lineno
            caller_filename = caller.f_code.co_filename

            caller_class = self.get_class_name(caller)
            caller_key_name = f"{caller_class}.{caller_func}"

            # record the call in the caller dict
            if self.traces.get(caller_key_name):
                # get the set of the functions called by the mother function and
                # add this current function
                callees = self.traces[caller_key_name]['calls']
                callees.add(key_name)
                self.traces[caller_key_name]['calls'] = callees

        else:
            pass
            # print(caller, func_name)

        self.traces[key_name] = dict(
            function_name=key_name,
            filename=func_filename.replace(self.cwd, ''),
            caller=caller_key_name,
            caller_line_num=caller_line_no,
            caller_file=caller_filename.replace(self.cwd, ''),
            line_num=func_line_no,
            call_args=arg_values,
            call_number=self.call_number,
            docstring=docstring,
            class_name=class_name,
            calls=OrderedSet(),
        )

        self.call_number += 1
        return self

    def get_docstring(self, func_name, frame):
        if func_name == '__init__':
            class_obj = self.get_class_obj(frame)
            docstring = class_obj.__doc__
        else:
            func_details = frame.f_globals.get(func_name)
            docstring = func_details.__doc__
        return docstring

    def handle_return(self, arg, key_name):

        # print('RETURN ARGS', key_name, arg)
        call_dict = self.traces.get(key_name, {})
        call_dict.update(
            dict(
                return_type=type(arg).__name__,
                # return_value=arg,
            )
        )
        self.traces[key_name] = call_dict
        return self

    def get_class_name(self, frame):
        class_obj = self.get_class_obj(frame)
        if class_obj:
            class_name = class_obj.__name__
        else:
            class_name = None
        return class_name

    def get_class_obj(self, frame):
        # initialize as None
        class_obj = None
        args, _, _, value_dict = inspect.getargvalues(frame)
        # we check the first parameter for the frame function is
        # named 'self'
        if len(args) and args[0] == 'self':
            # in that case, 'self' will be referenced in value_dict
            instance = value_dict.get('self', '')
            if instance:
                # return its class
                class_obj =  getattr(instance, '__class__', None)
        return class_obj
