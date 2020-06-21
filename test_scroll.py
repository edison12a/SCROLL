import sys
from scroll.tracer import Tracer
from demo import main
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

# do stuff with traces
collected_traces = manager.traces
pprint.pprint(collected_traces)

# get the leading/main function
collected_traces = {v['call_number']: v for k, v in collected_traces.items()}
keys = sorted(list(collected_traces))
for num in keys:
    if collected_traces[num]['calls']:
        main_method = collected_traces[num]['name']
        break

print(main_method)
