import sys
from scroll.tracer import Tracer
from example import main
import pprint


class MyContextManager():
    def __init__(self, Tracer):
        self.tracer = Tracer()

    def __enter__(self):
        # print('The context has been setup.')
        sys.settrace(self.tracer)
        return self.tracer

    def __exit__(self, type, value, traceback):
        # print(self.tracer.traces)
        print('Exiting the context.')
        # return None


with MyContextManager(Tracer) as manager:
    creds = main(1993, 71, 1.79)
# stop tracing
sys.settrace(None)

collected_traces = manager.traces
entry_point = manager.main_method
pprint.pprint(collected_traces)
print(entry_point)
