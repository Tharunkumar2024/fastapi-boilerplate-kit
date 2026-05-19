"""
The file have cli code for the boilerplate
"""

# pylint: disable=C0116,E1120,E1123

import os
import sys
import json
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


PRESETS = {
    "minimal": {
        "with_auth": False,
        "with_email": False,
        "with_tests": False,
        "database": "sqlite",
        "orm": "sqlalchemy",
        "database_path": "test.db",
    },
    "standard": {
        "with_auth": True,
        "with_email": True,
        "with_tests": True,
        "database": "sqlite",
        "orm": "sqlalchemy",
        "database_path": "test.db",
    },
    "enterprise": {
        "with_auth": True,
        "with_email": True,
        "with_tests": True,
        "database": "postgresql",
        "orm": "sqlalchemy",
        "database_host": "localhost",
        "database_port": 5432,
        "database_user": "postgres",
        "database_password": "postgres",
        "database_name": "app_db",
    },
}

RECOMMENDED_DEFAULTS = PRESETS["standard"].copy()


def _read_config_file(config_file):
    if not config_file:
        return {}

    try:
        with open(config_file, "r", encoding="utf-8-sig") as file:
            content = json.load(file)
    except FileNotFoundError as exc:
        raise click.ClickException(
            f"Config file not found: {config_file}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise click.ClickException(
            f"Invalid JSON config file: {config_file}"
        ) from exc

    if not isinstance(content, dict):
        raise click.ClickException("Config file must contain a JSON object.")
    return content


def _normalize_database_alias(database):
    if database == "postgres":
        return "postgresql"
    return database


def _resolve_config(
    *,
    project_name,
    with_auth,
    with_email,
    with_tests,
    database,
    orm,
    preset,
    config_file_data,
    database_path,
    database_host,
    database_port,
    database_user,
    database_password,
    database_name,
    interactive,
    yes,
):
    resolved = RECOMMENDED_DEFAULTS.copy()
    resolved.update(PRESETS[preset])
    resolved.update(config_file_data)

    explicit_overrides = {
        "with_auth": with_auth,
        "with_email": with_email,
        "with_tests": with_tests,
        "database": database,
        "orm": orm,
        "database_path": database_path,
        "database_host": database_host,
        "database_port": database_port,
        "database_user": database_user,
        "database_password": database_password,
        "database_name": database_name,
    }
    for key, value in explicit_overrides.items():
        if value is not None:
            resolved[key] = value

    resolved["database"] = _normalize_database_alias(resolved["database"])
    resolved["project_name"] = project_name

    should_prompt = bool(interactive) and not yes
    if should_prompt:
        resolved = _prompt_for_config(resolved)

    if resolved.get("with_auth"):
        resolved["with_email"] = True

    if resolved["database"] == "sqlite":
        for key in (
            "database_host",
            "database_port",
            "database_user",
            "database_password",
            "database_name",
        ):
            resolved.pop(key, None)
    else:
        resolved.pop("database_path", None)

    _validate_config(resolved)
    return resolved


def _prompt_for_config(resolved):
    use_preset = click.prompt(
        "Choose preset",
        type=click.Choice(["minimal", "standard", "enterprise", "custom"]),
        default="custom",
        show_choices=True,
    )
    if use_preset != "custom":
        merged = RECOMMENDED_DEFAULTS.copy()
        merged.update(PRESETS[use_preset])
        merged["project_name"] = resolved["project_name"]
        return merged

    resolved["database"] = click.prompt(
        "Database engine",
        type=click.Choice(["sqlite", "postgresql", "mysql"]),
        default=resolved.get("database", "sqlite"),
        show_choices=True,
    )
    resolved["orm"] = click.prompt(
        "ORM",
        type=click.Choice(["sqlalchemy"]),
        default=resolved.get("orm", "sqlalchemy"),
        show_choices=True,
    )

    if resolved["database"] == "sqlite":
        resolved["database_path"] = click.prompt(
            "SQLite database path",
            default=resolved.get("database_path", "test.db"),
        )
    else:
        resolved["database_host"] = click.prompt(
            "Database host",
            default=resolved.get("database_host", "localhost"),
        )
        resolved["database_port"] = click.prompt(
            "Database port",
            type=int,
            default=int(
                resolved.get(
                    "database_port",
                    5432 if resolved["database"] == "postgresql" else 3306,
                )
            ),
        )
        resolved["database_user"] = click.prompt(
            "Database username",
            default=resolved.get("database_user", "app_user"),
        )
        resolved["database_password"] = click.prompt(
            "Database password",
            default=resolved.get("database_password", "replace_with_password"),
            hide_input=True,
            show_default=False,
        )
        resolved["database_name"] = click.prompt(
            "Database name",
            default=resolved.get("database_name", "app_db"),
        )

    resolved["with_auth"] = click.confirm(
        "Enable auth module?",
        default=bool(resolved.get("with_auth", False)),
    )
    resolved["with_email"] = click.confirm(
        "Enable email module?",
        default=bool(resolved.get("with_email", False)),
    )
    resolved["with_tests"] = click.confirm(
        "Enable pytest scaffold?",
        default=bool(resolved.get("with_tests", False)),
    )
    return resolved


def _validate_config(resolved):
    database = resolved["database"]
    if database not in {"sqlite", "postgresql", "mysql"}:
        raise click.ClickException(
            "database must be one of sqlite, postgresql, mysql"
        )
    if resolved.get("orm") != "sqlalchemy":
        raise click.ClickException(
            "Only sqlalchemy ORM is supported currently."
        )

    if database == "sqlite":
        if not resolved.get("database_path"):
            raise click.ClickException(
                "database_path is required for sqlite configuration."
            )
        return

    required_fields = [
        "database_host",
        "database_port",
        "database_user",
        "database_password",
        "database_name",
    ]
    missing_fields = [
        field for field in required_fields if not resolved.get(field)
    ]
    if missing_fields:
        raise click.ClickException(
            "Missing database configuration values: "
            + ", ".join(missing_fields)
        )


def _print_resolved_config(resolved):
    sanitized = resolved.copy()
    if sanitized.get("database_password"):
        sanitized["database_password"] = "******"
    click.echo("Resolved configuration:")
    click.echo(json.dumps(sanitized, indent=2, sort_keys=True))


@cli.command()
@click.argument('project_name')
@click.option("--with-auth/--without-auth", default=None)
@click.option("--with-email/--without-email", default=None)
@click.option("--with-tests/--without-tests", default=None)
@click.option(
    "--database",
    type=click.Choice(["sqlite", "postgresql", "postgres", "mysql"]),
    default=None,
)
@click.option(
    "--orm",
    type=click.Choice(["sqlalchemy"]),
    default=None,
)
@click.option(
    "--preset",
    type=click.Choice(["minimal", "standard", "enterprise"]),
    default="standard",
    show_default=True,
)
@click.option("--config-file", type=click.Path(exists=True), default=None)
@click.option(
    "--interactive/--no-interactive",
    default=False,
    show_default=True,
)
@click.option("--yes", is_flag=True, default=False)
@click.option("--dry-run", is_flag=True, default=False)
@click.option("--database-path", default=None)
@click.option("--database-host", default=None)
@click.option("--database-port", type=int, default=None)
@click.option("--database-user", default=None)
@click.option("--database-password", default=None)
@click.option("--database-name", default=None)
def generate(
    project_name,
    with_auth,
    with_email,
    with_tests,
    database,
    orm,
    preset,
    config_file,
    interactive,
    yes,
    dry_run,
    database_path,
    database_host,
    database_port,
    database_user,
    database_password,
    database_name,
):
    """Generate a FastAPI boilerplate project with the specified project name.

    Args:\n
    project_name (str): The name of the project to be generated.

    This command will create the necessary directory structure and files
    for a FastAPI project with a basic setup.
    """
    config_file_data = _read_config_file(config_file)
    resolved = _resolve_config(
        project_name=project_name,
        with_auth=with_auth,
        with_email=with_email,
        with_tests=with_tests,
        database=database,
        orm=orm,
        preset=preset,
        config_file_data=config_file_data,
        database_path=database_path,
        database_host=database_host,
        database_port=database_port,
        database_user=database_user,
        database_password=database_password,
        database_name=database_name,
        interactive=interactive,
        yes=yes,
    )
    _print_resolved_config(resolved)
    if dry_run:
        click.echo("Dry run enabled. No files were generated.")
        return

    print("Generating project with selected boilerplate options.")
    generate_project(
        project_name=resolved["project_name"],
        with_auth=resolved["with_auth"],
        with_email=resolved["with_email"],
        with_tests=resolved["with_tests"],
        db_config=resolved["database"],
        db_settings=resolved,
    )


if __name__ == '__main__':
    cli()
