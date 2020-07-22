import sys
from scroll.tracer import Tracer
from scroll.runner import RuntimeContextManager
from demo.demo import main
import pprint
from scroll.generators import generate_docs


if __name__ == '__main__':
    with RuntimeContextManager(Tracer) as manager:
        creds = main(1993, 71, 1.79)
    # stop tracing
    sys.settrace(None)

    # do stuff with traces
    collected_traces = manager.traces
    pprint.pprint(collected_traces)
    generate_docs(collected_traces, directory='demo')
