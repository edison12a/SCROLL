"""SCROLL: Automatically generates documentation and unit-tests for python programs"""
__version__ = "2020.6.25"

import sys
import click
import runpy
from scroll.runner import MyContextManager
from scroll.tracer import Tracer
from scroll.generators import generate_docs
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
    # write assets to files
    generate_docs(collected_traces)
