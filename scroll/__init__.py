"""SCROLL: Automatically generates documentation and unit-tests for python programs"""
__version__ = "2020.7.22"

import os
import sys
import click
import runpy
from scroll.runner import RuntimeContextManager
from scroll.tracer import Tracer
from scroll.generators import generate_docs
import pprint


@click.command()
@click.argument('filename')
def scroll(filename):
    """This is the main controller of the app.
        It aslo responds to commandline args using click
    """
    click.echo(f'SCROLL: Running file {filename}')
    # use a context manager to enter the file runtime and introspect it
    with RuntimeContextManager(Tracer) as manager:
        runpy.run_path(filename, run_name='__main__')
    sys.settrace(None)
    click.echo(f'SCROLL: Traces collected')
    collected_traces = manager.traces
    pprint.pprint(collected_traces)
    # generate docs and write to files
    directory = os.path.dirname(filename)
    generate_docs(collected_traces, directory)
    click.echo(f'SCROLL: Finished generating docs at docs/index.html')
