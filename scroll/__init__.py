"""SCROLL: Automatically generates documentation and unit-tests for python programs"""
__version__ = "2020.6.16"

import sys
import click
import runpy
from scroll.runner import MyContextManager
from scroll.tracer import Tracer
import pprint


@click.command()
@click.argument('filename')
def scroll(filename):
    """Print FILENAME."""
    click.echo(filename)
    with MyContextManager(Tracer) as manager:
        runpy.run_path(filename, run_name='__main__')
    sys.settrace(None)

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
