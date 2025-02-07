"""
The file have cli code for the boilerplate
"""

# pylint: disable=C0116,E1120

import os
import sys
import click
from fastapi_boilerplate_kit.generate import generate_project

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


@click.group()
def cli():
    """Main command group for fastapi-boilerplate."""


@cli.command()
@click.argument('project_name')
@click.option(
    '--sqlalchemy',
    is_flag=True,
    default=False,
    help='Include SQLAlchemy in the generated project'
)
@click.option(
    '--alembic',
    is_flag=True,
    default=False,
    help='Include Alembic in the generated project'
)
def generate(project_name, sqlalchemy, alembic):
    if sqlalchemy and alembic:
        print("Generating project with SQLAlchemy and Alembic.")
        generate_project(project_name, sqlalchemy=True, alembic=True)
    elif sqlalchemy:
        print("Generating project with SQLAlchemy.")
        generate_project(project_name, sqlalchemy=True, alembic=False)
    elif alembic:
        print("Generating project with Alembic.")
        generate_project(project_name, sqlalchemy=False, alembic=True)
    else:
        print("Generating project without SQLAlchemy or Alembic.")
        generate_project(project_name, sqlalchemy=False, alembic=False)

if __name__ == '__main__':
    cli()
