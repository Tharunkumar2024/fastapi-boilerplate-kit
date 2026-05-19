# FastAPI Boilerplate Kit

<p align="center">
  <strong>CLI scaffolding for production-ready FastAPI applications</strong><br>
  Auth, RBAC, JWT middleware, multi-database presets, and pytest - generated with one command.
</p>

<p align="center">
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/"><img src="https://img.shields.io/pypi/v/fastapi-boilerplate-kit?label=PyPI&logo=python&logoColor=white" alt="PyPI version"></a>
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/"><img src="https://img.shields.io/pypi/pyversions/fastapi-boilerplate-kit" alt="Python versions"></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/pypi/l/fastapi-boilerplate-kit" alt="License"></a>
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/"><img src="https://img.shields.io/pypi/format/fastapi-boilerplate-kit" alt="Package format"></a>
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/"><img src="https://img.shields.io/pypi/dm/fastapi-boilerplate-kit" alt="PyPI downloads"></a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/actions/workflows/publish.yml"><img src="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/actions/workflows/publish.yml/badge.svg" alt="Publish to PyPI"></a>
</p>

<p align="center">
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub repository">
  </a>
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/">
    <img src="https://img.shields.io/badge/PyPI-Install-3775A9?style=flat-square&logo=pypi&logoColor=white" alt="PyPI package">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/docs/cli.md">
    <img src="https://img.shields.io/badge/CLI-Documentation-007ACC?style=flat-square&logo=markdown&logoColor=white" alt="CLI documentation">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/CHANGELOG.md">
    <img src="https://img.shields.io/badge/Changelog-Release%20notes-5C4EE5?style=flat-square&logo=semanticrelease&logoColor=white" alt="Changelog">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/issues">
    <img src="https://img.shields.io/badge/Issues-Get%20help-D73A4A?style=flat-square&logo=githubissues&logoColor=white" alt="GitHub issues">
  </a>
</p>

---

**FastAPI Boilerplate Kit** (`dnd`) is a PyPI package that generates opinionated, deployment-oriented FastAPI project layouts-routing, persistence, authentication, and tests - so you can focus on business logic instead of repetitive setup.

```bash
pip install fastapi-boilerplate-kit
dnd generate my_app --yes
```

## Features
- **FastAPI Boilerplate**: A clean project setup for building FastAPI applications quickly.
- **Auth Module**: Register, login, refresh, forgot/reset password, change password, and invite flows.
- **Auth Middleware + Authorization**: JWT middleware with dependency-based authorization guards.
- **Scoped Access Querying**: Repository/service-level scope-aware filtering patterns.
- **Email Integration**: Async email service templates for auth and integration use cases.
- **Test Scaffold (PyTest)**: Baseline test structure with API/service test examples.
- **Interactive Scaffolding**: Guided generation with `--interactive`.
- **Config-Driven Scaffolding**: Deterministic generation with `--config-file`.
- **Preset Modes**: `minimal`, `standard`, and `enterprise`.
- **Database-Aware Generation**: Supports SQLite and server DB style setup (PostgreSQL/MySQL).

## Getting Started

### Installation Instructions:
To install the FastAPI Boilerplate Kit, run:

```
pip install fastapi-boilerplate-kit
```

Alternatively, you can install from the test PyPI repository for testing purposes:

```
pip install -i https://test.pypi.org/simple/ fastapi-boilerplate-kit
```

### Generate a New Project
Once the installation is complete, generate a project with:

```bash
dnd generate PROJECT_NAME
```

This creates `PROJECT_NAME` with recommended defaults (`sqlalchemy`, `sqlite`, auth/email/tests enabled).

### What gets scaffolded

- API routing with public/protected separation
- Auth endpoints and auth token workflow
- JWT + password security utilities
- Middleware + dependency layers for auth/authorization
- Repositories/services with scoped querying pattern
- PyTest baseline and sample tests
- Environment and DB configuration templates

### Project Setup
1. **Change to the generated project directory**:
```
cd PROJECT_NAME
```

2. **Install dependencies**:
```
pip install -r requirements.txt
```

3. **Start the FastAPI server**:
```
python main.py
```

4. **Access the Swagger Docs**: Open your browser and navigate to:
```
http://localhost:8000/docs
```

This will give you access to FastAPI's interactive API documentation.

### Project Example:
For example, after generating a project named `test_project`, the following steps are needed:
1. Change directory:
```
cd test_project
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Start the FastAPI server:
```
python main.py
```

4. Visit the Swagger docs at `http://localhost:8000/docs` for detailed API documentation.

## Command-Line Interface (CLI)
The FastAPI Boilerplate Kit provides a CLI to simplify project generation.

### Core Command

```bash
dnd generate PROJECT_NAME [options]
```

### Common Workflows

1. **Default generation (recommended defaults)**

```bash
dnd generate my_app
```

2. **Interactive guided setup**

```bash
dnd generate my_app --interactive
```

3. **Non-interactive with explicit DB settings**

```bash
dnd generate my_app --yes --database postgresql --database-host localhost --database-port 5432 --database-user app_user --database-password app_pass --database-name app_db
```

4. **Dry run (preview resolved config without writing files)**

```bash
dnd generate my_app --yes --database mysql --database-host localhost --database-port 3306 --database-user root --database-password root --database-name app_db --dry-run
```

### Using `--config-file`

You can pass a JSON file to keep generation deterministic across environments and teams.

Example file `scaffold.config.json`:

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

Generate from config:

```bash
dnd generate my_app --config-file scaffold.config.json --yes
```

### Key Options

- `--interactive`: guided prompts for preset, DB, and features
- `--yes`: accept defaults and skip prompts
- `--dry-run`: print resolved config and skip file generation
- `--preset {minimal|standard|enterprise}`: start from curated defaults
- `--database {sqlite|postgresql|postgres|mysql}`
- SQLite option: `--database-path`
- Server DB options: `--database-host`, `--database-port`, `--database-user`, `--database-password`, `--database-name`
- Feature toggles: `--with-auth/--without-auth`, `--with-email/--without-email`, `--with-tests/--without-tests`

For advanced examples and CI usage, see [`docs/cli.md`](docs/cli.md).

### Version Information
You can check the version of the FastAPI Boilerplate Kit using:

```
dnd --version
```

or

```
dnd -V
```

This will show the installed version of the `fastapi-boilerplate-kit`.

<br>

## Production notes

<details>
<summary><strong>Operational defaults & SuperAdmin bootstrap</strong></summary>

<br>

**General**

- Current ORM support is `sqlalchemy`.
- If auth is enabled, email is enabled automatically by design.

**Initial SuperAdmin (generated apps)**

- Seeding creates **roles** (`SuperAdmin`, `User`) by default. The `User` role is the default for **self-service** `POST /auth/register` (least privilege). You may rename or delete the `User` role via the roles API; if it is missing, open registration returns **409** until you recreate a role named `User` (or use invite-only onboarding).
- At most **one** user may hold the `SuperAdmin` role at a time (enforced on register-with-invite, invite, admin user create/update, and optional env bootstrap). The `SuperAdmin` **role** cannot be deleted via API; **SuperAdmin users** cannot be deleted via API (profile and password flows still apply). Offboarding or GDPR-style erasure may require a controlled DB or support process.
- Optional bootstrap (`ENABLE_SEED=TRUE`, no SuperAdmin yet): set **`ADMIN_PASSWORD`** for a fixed first password, or leave it **empty** for a **mandatory** one-time generated password. Stored value is always a hash; **`must_change_password`** applies until `POST /api/v1/auth/change-password`.
- **`ADMIN_PASSWORD` empty:** a one-time random password is generated on first successful seed and **printed to stdout** (treat logs as sensitive). An explicit **`ADMIN_PASSWORD`** always wins. **`POST /api/v1/users`** cannot assign `SuperAdmin`—first admin comes from seed or controlled DB access.

</details>

<br>

---

<br>

<p align="center">
  <strong>Project information</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://pypi.org/project/fastapi-boilerplate-kit/"><img src="https://img.shields.io/badge/distribution-PyPI-3775A9?style=flat-square&logo=pypi&logoColor=white" alt="PyPI distribution"></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/stack-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"></a>
</p>

<br>

<details>
<summary><strong>Development setup</strong></summary>

<br>

```bash
git clone https://github.com/Tharunkumar2024/fastapi-boilerplate-kit.git
cd fastapi-boilerplate-kit
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -e .
dnd --version
```

Build a wheel locally:

```bash
pip install setuptools wheel
python setup.py sdist bdist_wheel
```

</details>

<br>

<p align="center">
  <strong>Community</strong>
</p>

<p align="center">
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/Contributing-Guidelines-2EA44F?style=flat-square&logo=github&logoColor=white" alt="Contributing guidelines">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/SECURITY.md">
    <img src="https://img.shields.io/badge/Security-Policy-BC245B?style=flat-square&logo=dependabot&logoColor=white" alt="Security policy">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/issues">
    <img src="https://img.shields.io/badge/Issues-Support-D73A4A?style=flat-square&logo=githubissues&logoColor=white" alt="GitHub issues">
  </a>
  <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/CHANGELOG.md">
    <img src="https://img.shields.io/badge/Changelog-v1.6.0-5C4EE5?style=flat-square&logo=semanticrelease&logoColor=white" alt="Changelog">
  </a>
</p>

<p align="center">
  <sub>
    Report vulnerabilities privately via
    <a href="mailto:tharunkumar.developers@gmail.com">email</a>
    or
    <a href="https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/security/advisories/new">GitHub Security Advisories</a>
    — do not use public issues for security reports.
  </sub>
</p>

<br>

<p align="center">
  <strong>Built with</strong>
</p>

<p align="center">
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://click.palletsprojects.com/"><img src="https://img.shields.io/badge/Click-CLI-000000?style=for-the-badge&logo=click&logoColor=white" alt="Click"></a>
  <a href="https://jinja.palletsprojects.com/"><img src="https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2"></a>
</p>

<br>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-2F80ED?style=flat-square&logo=apache&logoColor=white" alt="Apache 2.0 License">
  </a>
</p>

<p align="center">
  <sub>
    <strong>FastAPI Boilerplate Kit</strong> · maintained by
    <a href="https://github.com/Tharunkumar2024"><strong>Tharunkumar Saravanan</strong></a>
  </sub>
</p>

<p align="center">
  <sub>© 2025–2026 Tharunkumar Saravanan · Apache License 2.0</sub>
</p>
