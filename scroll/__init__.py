"""SCROLL: Automatically generates documentation and unit-tests for python programs"""
__version__ = "2020.6.16"

import sys
import click
import runpy
from scroll.runner import MyContextManager
from scroll.tracer import Tracer


@click.command()
@click.argument('filename')
def scroll(filename):
    """Print FILENAME."""
    click.echo(filename)
    with MyContextManager(Tracer) as manager:
        runpy.run_path(filename, run_name='__main__')
    sys.settrace(None)
    print(manager.traces)
    print(manager.main_method)
