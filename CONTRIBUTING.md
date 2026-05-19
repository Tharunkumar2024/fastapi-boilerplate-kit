# Contributing

Thank you for your interest in contributing to FastAPI Boilerplate Kit.

## Branch flow

1. Branch from `develop` (for example `feature/my-change`).
2. Open a pull request into `develop`.
3. Release branches (for example `release/1.6.0`) are used to stabilize and ship to `main` and PyPI.

Do not open feature PRs directly against `main` unless it is an urgent hotfix agreed in an issue.

## Local setup

```bash
git clone https://github.com/Tharunkumar2024/fastapi-boilerplate-kit.git
cd fastapi-boilerplate-kit
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
dnd --version
```

## Making changes

- Update templates under `fastapi_boilerplate_kit/templates/` when changing generated app behavior.
- Keep `setup.py` and `fastapi_boilerplate_kit/__init__.py` versions aligned when preparing a release.
- Update `CHANGELOG.md` under **Unreleased** or the target version section.
- Run a quick smoke test after CLI changes:

  ```bash
  dnd generate smoke_test --dry-run
  dnd generate smoke_test --yes
  ```

## Pull requests

- Use a clear title and description.
- Link related issues when applicable.
- Ensure generated projects still start and tests pass when you touch templates or core generator logic.

## Releases

Maintainers cut releases from `release/*` branches, merge to `main`, tag `v*`, and publish to PyPI via GitHub Actions.
