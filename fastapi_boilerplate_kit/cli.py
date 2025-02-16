"""
The file have cli code for the boilerplate
"""

# pylint: disable=C0116,E1120

import os
import sys
import click
from fastapi_boilerplate_kit.generate import generate_project
from fastapi_boilerplate_kit import __version__

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def print_version(ctx, _, value):
    """Print the version of the fastapi-boilerplate-kit and exit."""
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'DND(fastapi-boilerplate-kit) {__version__}')
    ctx.exit()


@click.group(invoke_without_command=True)
@click.option(
    '-V',
    '--version',
    is_flag=True,
    callback=print_version,
    help='Show the version and exit.',
    expose_value=False,
    is_eager=True
)
def cli():
    """
    Main command group for fastapi-boilerplate.
    
    This tool generates a basic FastAPI project boilerplate.
    """

@cli.command()
@click.argument('project_name')
def generate(project_name):
    """Generate a FastAPI boilerplate project with the specified project name.

    Args:\n
    project_name (str): The name of the project to be generated.
    
    This command will create the necessary directory structure and files
    for a FastAPI project with a basic setup.
    """
    print("Generating project with default basic setup.")
    generate_project(project_name)


if __name__ == '__main__':
    cli()
