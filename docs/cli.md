# CLI Advanced Usage

This guide covers advanced usage patterns for the `dnd` CLI.

## Scope

The CLI can scaffold more than base routing. Depending on selected options, it can include:

- email integration scaffolding
- auth middleware and authorization dependencies
- scoped access query patterns
- pytest scaffold
- full auth endpoint set including refresh flow

## Command

```bash
dnd generate PROJECT_NAME [options]
```

## Resolution Precedence

When multiple configuration sources are provided, values are resolved in this order:

1. Explicit CLI options
2. `--config-file` values
3. `--preset` values
4. Recommended defaults

## Presets

- `minimal`
  - `with_auth=false`, `with_email=false`, `with_tests=false`
  - `database=sqlite`, `orm=sqlalchemy`
- `standard` (default)
  - `with_auth=true`, `with_email=true`, `with_tests=true`
  - `database=sqlite`, `orm=sqlalchemy`
- `enterprise`
  - `with_auth=true`, `with_email=true`, `with_tests=true`
  - `database=postgresql`, `orm=sqlalchemy`

## Interactive vs Non-Interactive

- `--interactive`: prompts for preset, DB, and feature toggles
- `--yes`: disables prompts and accepts resolved defaults
- `--dry-run`: prints resolved config and skips writing files

## Database Configuration Model

### SQLite

Use path-based config:

```bash
dnd generate my_app --yes --database sqlite --database-path app.db
```

### Server Databases (PostgreSQL/MySQL)

Use credential and host config:

```bash
dnd generate my_app --yes --database postgresql --database-host localhost --database-port 5432 --database-user app_user --database-password app_pass --database-name app_db
```

```bash
dnd generate my_app --yes --database mysql --database-host localhost --database-port 3306 --database-user root --database-password root --database-name app_db
```

## Config File Workflow

Create a JSON file, for example `scaffold.config.json`:

```json
{
  "preset": "standard",
  "database": "postgresql",
  "orm": "sqlalchemy",
  "with_auth": true,
  "with_email": true,
  "with_tests": true,
  "database_host": "localhost",
  "database_port": 5432,
  "database_user": "app_user",
  "database_password": "app_pass",
  "database_name": "app_db"
}
```

Use it:

```bash
dnd generate my_app --config-file scaffold.config.json --yes
```

Override selected values from CLI:

```bash
dnd generate my_app --config-file scaffold.config.json --database mysql --database-port 3306 --yes
```

## CI/CD Examples

### GitHub Actions step

```bash
python -m pip install fastapi-boilerplate-kit
dnd generate generated_app --config-file scaffold.config.json --yes
```

### Preview in CI without writing files

```bash
dnd generate generated_app --config-file scaffold.config.json --yes --dry-run
```

## Notes

- `--database postgres` is accepted as an alias and normalized to `postgresql`.
- If auth is enabled, email is enabled automatically.
- Only `sqlalchemy` ORM is currently supported.
- `--config-file` JSON may be UTF-8 with or without a BOM (e.g. files created via PowerShell `Set-Content -Encoding utf8`).

## Version

This CLI behavior is documented for release `1.6.0` and later.
