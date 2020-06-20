import click
import runpy
from scroll.runner import MyContextManager


@click.command()
@click.argument('filename')
def scroll(filename):
    """Print FILENAME."""
    click.echo(filename)
    with MyContextManager() as manager:
        runpy.run_path(filename, run_name='__main__')
    print(manager.traces)
