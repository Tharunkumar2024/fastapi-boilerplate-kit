# Changelog

## Version 1.6.0 Release Notes - 2026-04-25 (stable)

### Added:
- Enhanced `dnd generate` UX with interactive mode (`--interactive`), dry-run mode, presets, and JSON `--config-file` support.
- Added resolved-configuration output to improve CLI transparency before generation.
- Added database-aware generation flow for `sqlite`, `postgresql`, and `mysql`.
- Added shared server-DB templates to reuse MySQL/PostgreSQL logic and included `pymysql` dependency for MySQL support.
- Added dedicated CLI usage documentation in `README.md` and `docs/cli.md` with config precedence and CI examples.
- Added email integration templates and wiring for auth/integration flows.
- Added JWT auth middleware and dependency-based authorization templates.
- Added scoped access querying support patterns in repository/service layers.
- Added PyTest scaffold templates for health/API/service testing.
- Added complete auth endpoint set including refresh token flow.

### Changed:
- Consolidated MySQL/PostgreSQL DB template handling into shared server-DB partials to reduce duplication.
- Updated project documentation to reflect current feature set, commands, and release status.
- **Bootstrapping:** user seeding is roles-only by default; first SuperAdmin from `ADMIN_EMAIL` uses `ADMIN_PASSWORD` when set, otherwise **always** a one-time generated password when `ADMIN_PASSWORD` is empty (never skipped); `must_change_password` until change-password.
- **RBAC:** seeded `User` role for default self-service registration; at most one `SuperAdmin` user; SuperAdmin user/role delete blocked via API; env bootstrap skipped only if a SuperAdmin already exists; user admin routes (`POST`/`PATCH`/`DELETE` users, `GET /users/{id}`) require SuperAdmin; `POST /users` cannot assign SuperAdmin (first admin from seed or break-glass only).

## Unreleased

### Planned:
- Continue expanding optional generators and integrations.

## Version 1.5.8 Release Notes - 2025-02-16 (stable)

### Added:
- Initial Release of the FastAPI Boilerplate Kit:
  - **Core package structure:** Provides a solid foundation for creating FastAPI applications.
  - Basic functions or classes to get started quickly with FastAPI projects.
  - **CLI tool:** Allows project generation with a single command.
  - Pre-configured templates for key files like main.py, Dockerfile, and requirements.txt.
  - Swagger UI integration for automatic API documentation at http://localhost:8000/docs.
  - Installation instructions and easy setup process, including clear steps for setting up dependencies and starting the server.

### Features:
- **Pre-configured templates:**
  - Templates for essential project files such as main.py, Dockerfile, and requirements.txt.
- **Command-Line Interface (CLI):**
  - Use `dnd generate PROJECT_NAME` to automatically generate a FastAPI project with a predefined structure.
- **Swagger UI:** Automatically accessible at http://localhost:8000/docs for API documentation.

### Known Issues:
- N/A (First release).

### Future Improvements:
- Initial roadmap captured for upcoming releases.
