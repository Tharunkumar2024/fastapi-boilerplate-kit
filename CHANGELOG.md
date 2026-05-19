# Changelog

All notable changes to this project are documented in this file.

## Unreleased

### Planned
- Continue expanding optional generators and integrations.

## Version 1.6.0 Release Notes - 2026-05-19 (stable)

### Added
- Enhanced `dnd generate` UX with interactive mode (`--interactive`), dry-run mode (`--dry-run`), presets (`minimal`, `standard`, `enterprise`), and JSON `--config-file` support.
- Resolved-configuration output before generation (passwords masked in CLI output).
- Database-aware generation for `sqlite`, `postgresql` (`postgres` alias), and `mysql`.
- Shared server-DB templates for MySQL/PostgreSQL; `pymysql` in generated `requirements.txt` when applicable.
- Dedicated CLI documentation in `README.md` and `docs/cli.md` (config precedence, CI examples).
- Email integration templates for auth and integration flows.
- JWT auth middleware and dependency-based authorization guards.
- Scoped access querying patterns in repository/service layers.
- PyTest scaffold templates (health, users, auth, services).
- Complete auth endpoint set: register, login, refresh, forgot/reset/change password, invite.
- Initial SuperAdmin env bootstrap (`initial_admin_seeder`) with `must_change_password` until change-password.

### Changed
- Consolidated MySQL/PostgreSQL DB template handling into shared server-DB partials.
- Updated project documentation for the current feature set and CLI commands.
- **Bootstrapping:** user seeding is roles-only by default; first SuperAdmin from `ADMIN_EMAIL` uses `ADMIN_PASSWORD` when set, otherwise **always** a one-time generated password when `ADMIN_PASSWORD` is empty (never skipped).
- **RBAC:** seeded `User` role for default self-service registration; at most one `SuperAdmin` user; SuperAdmin user/role delete blocked via API; env bootstrap skipped only if a SuperAdmin already exists; user admin routes (`POST`/`PATCH`/`DELETE` users, `GET /users/{id}`) require SuperAdmin; `POST /users` cannot assign SuperAdmin (first admin from seed or controlled DB only).
- Auth message endpoints (`forgot-password`, `reset-password`, `change-password`, `invite`) return top-level `message` with `data: null` (no nested `data.message`).
- **Packaging:** wheel/sdist include all nested templates (`templates/**/*.jinja`); removed stale `py_modules=['cli']` from `setup.py`.
- **CLI:** `--config-file` accepts UTF-8 JSON with or without BOM (`utf-8-sig`).

### Fixed
- Generated `app/seeds/__init__.py` exports `seed_initial_admin` when auth is enabled.
- Generator passes template context for conditional seed imports.

## Version 1.5.8 Release Notes - 2025-02-16 (stable)

### Added
- Initial release of the FastAPI Boilerplate Kit:
  - **Core package structure** for FastAPI applications.
  - **CLI tool:** `dnd generate PROJECT_NAME` for project scaffolding.
  - Pre-configured Jinja templates for `main.py`, `requirements.txt`, and project layout.
  - Swagger UI at `http://localhost:8000/docs` in generated apps.

### Features
- **Pre-configured templates** for essential project files.
- **Command-line interface** for one-command project generation.
- **Swagger UI** integration in generated applications.

### Known Issues
- N/A (first release).

### Future Improvements
- Initial roadmap captured for upcoming releases.
