import sys
import json
from tracer import Tracer
from example import main


class MyContextManager():
    def __init__(self):
        self.tracer = Tracer()

    def __enter__(self):
        # print('The context has been setup.')
        sys.settrace(self.tracer)
        return self.tracer

    def __exit__(self, type, value, traceback):
        # print(self.tracer.traces)
        print('Exiting the context.')


with MyContextManager() as manager:
    creds = main(1993, 71, 1.79)
    
print(manager.traces)
