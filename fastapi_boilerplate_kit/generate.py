"""
The file have generation code for the boilerplate
"""

# pylint: disable=C0116,R0913,R0917

import os
from jinja2 import Environment, PackageLoader


def generate_project(
    project_name,
    with_auth=False,
    with_email=False,
    with_tests=False,
    db_config="sqlite",
    db_settings=None,
):
    if with_auth:
        with_email = True

    project_dir = project_name
    feature_context = {
        "project_name": project_name,
        "with_auth": with_auth,
        "with_email": with_email,
        "with_tests": with_tests,
        "db_config": db_config,
    }
    if db_settings:
        feature_context.update(db_settings)

    # Set up the Jinja environment
    env = Environment(
        loader=PackageLoader("fastapi_boilerplate_kit", "templates")
    )

    # Create directory structure
    create_directories(
        project_dir,
        with_auth=with_auth,
        with_tests=with_tests,
    )

    # Generate FastAPI app entry point (main.py)
    create_file_from_template(
        env,
        "main.py.jinja",
        os.path.join(project_dir, "main.py"),
        feature_context,
    )

    # Generate environment variables
    generate_env(
        project_dir,
        env,
        db_config=db_config,
        context=feature_context,
    )

    # Generate basic files
    create_basic_files(project_dir, env, context=feature_context)

    # Generate core files
    create_core_files(project_dir, env, context=feature_context)

    # Generate db files
    create_db_files(
        project_dir,
        env,
        db_config=db_config,
        context=feature_context,
    )

    # Generate API files
    create_api_files(project_dir, env, context=feature_context)

    # Generate utils files
    create_utils_files(project_dir, env)

    # Optional features
    if with_auth:
        create_auth_files(project_dir, env, context=feature_context)
    if with_email:
        create_email_files(project_dir, env, context=feature_context)
    if with_tests:
        create_test_files(project_dir, env, context=feature_context)

    print(
        "Successfully generated the FastAPI boilerplate "
        f"template to your project - {project_dir}"
    )


def create_directories(base_path, with_auth=False, with_tests=False):
    dirs = [
        "app",
        "app/api/v1",
        "app/common",
        "app/core",
        "app/database",
        "app/integrations",
        "app/migrations",
        "app/models",
        "app/repositories",
        "app/schemas",
        "app/seeds",
        "app/services",
        "app/tasks",
        "utils",
        "utils/global_handlers",
    ]
    if with_auth:
        dirs.extend(
            [
                "app/dependencies",
                "app/middlewares",
                "app/security",
            ]
        )
    if with_tests:
        dirs.extend(
            [
                "tests",
                "tests/api",
                "tests/services",
            ]
        )

    for dir_ in dirs:
        os.makedirs(os.path.join(base_path, dir_), exist_ok=True)


def create_file(file_path, content):
    """Helper function to create a file and write content"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        f.write("\n")


def create_file_from_template(env, template_name, file_path, context):
    """Render a Jinja template and create a file"""
    template = env.get_template(template_name)
    rendered_content = template.render(context)
    create_file(file_path, rendered_content)


def generate_env(project_dir, env, db_config="sqlite", context=None):
    """Generate .env configuration"""
    template_context = {"db_config": db_config}
    if context:
        template_context.update(context)

    create_file_from_template(
        env,
        ".env.jinja",
        os.path.join(project_dir, ".env"),
        template_context,
    )


def create_basic_files(project_dir, env, context):
    """Generate basic files for the project"""
    create_file_from_template(
        env,
        "requirements.txt.jinja",
        os.path.join(project_dir, "requirements.txt"),
        context,
    )
    create_file_from_template(
        env,
        "README.md.jinja",
        os.path.join(project_dir, "README.md"),
        {"project_name": project_dir},
    )
    create_file_from_template(
        env, ".pylintrc.jinja", os.path.join(project_dir, ".pylintrc"), {}
    )
    create_file_from_template(
        env, ".gitignore.jinja", os.path.join(project_dir, ".gitignore"), {}
    )
    create_file_from_template(
        env, "__init__.py.jinja", os.path.join(project_dir, "__init__.py"), {}
    )


def create_utils_files(project_dir, env):
    """Generate utils files"""
    create_file_from_template(
        env,
        "utils/global_handlers/error_handler.py.jinja",
        os.path.join(project_dir, "utils/global_handlers/error_handler.py"),
        {},
    )


def create_db_files(project_dir, env, db_config="sqlite", context=None):
    """Generate database files"""
    template_context = {"db_config": db_config}
    if context:
        template_context.update(context)

    create_file_from_template(
        env,
        "app/database/__init__.py.jinja",
        os.path.join(project_dir, "app/database/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/database/config.py.jinja",
        os.path.join(project_dir, "app/database/config.py"),
        template_context,
    )
    create_file_from_template(
        env,
        "app/database/database.py.jinja",
        os.path.join(project_dir, "app/database/database.py"),
        template_context,
    )


def create_core_files(project_dir, env, context):
    """Generate core files"""
    create_file_from_template(
        env,
        "app/core/__init__.py.jinja",
        os.path.join(project_dir, "app/core/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/core/config.py.jinja",
        os.path.join(project_dir, "app/core/config.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/core/constants.py.jinja",
        os.path.join(project_dir, "app/core/constants.py"),
        {},
    )


def create_api_files(project_dir, env, context):
    """Generate API routes, services, repositories, schemas and models files"""
    create_file_from_template(
        env,
        "app/models/__init__.py.jinja",
        os.path.join(project_dir, "app/models/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/models/base_model.py.jinja",
        os.path.join(project_dir, "app/models/base_model.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/models/roles.py.jinja",
        os.path.join(project_dir, "app/models/roles.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/models/users.py.jinja",
        os.path.join(project_dir, "app/models/users.py"),
        context,
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "app/models/auth_tokens.py.jinja",
            os.path.join(project_dir, "app/models/auth_tokens.py"),
            context,
        )
    create_file_from_template(
        env,
        "app/repositories/__init__.py.jinja",
        os.path.join(project_dir, "app/repositories/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/repositories/roles.py.jinja",
        os.path.join(project_dir, "app/repositories/roles.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/repositories/users.py.jinja",
        os.path.join(project_dir, "app/repositories/users.py"),
        context,
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "app/repositories/scopes.py.jinja",
            os.path.join(project_dir, "app/repositories/scopes.py"),
            context,
        )
        create_file_from_template(
            env,
            "app/repositories/auth.py.jinja",
            os.path.join(project_dir, "app/repositories/auth.py"),
            context,
        )
    create_file_from_template(
        env,
        "app/schemas/__init__.py.jinja",
        os.path.join(project_dir, "app/schemas/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/schemas/roles.py.jinja",
        os.path.join(project_dir, "app/schemas/roles.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/schemas/users.py.jinja",
        os.path.join(project_dir, "app/schemas/users.py"),
        {},
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "app/schemas/auth.py.jinja",
            os.path.join(project_dir, "app/schemas/auth.py"),
            context,
        )
    create_file_from_template(
        env,
        "app/schemas/commons/__init__.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/schemas/commons/base_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/base_response.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/schemas/commons/role_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/role_response.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/schemas/commons/user_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/user_response.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/seeds/__init__.py.jinja",
        os.path.join(project_dir, "app/seeds/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/seeds/roles_seeder.py.jinja",
        os.path.join(project_dir, "app/seeds/roles_seeder.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/seeds/users_seeder.py.jinja",
        os.path.join(project_dir, "app/seeds/users_seeder.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/services/__init__.py.jinja",
        os.path.join(project_dir, "app/services/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/services/roles.py.jinja",
        os.path.join(project_dir, "app/services/roles.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/services/users.py.jinja",
        os.path.join(project_dir, "app/services/users.py"),
        context,
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "app/services/auth.py.jinja",
            os.path.join(project_dir, "app/services/auth.py"),
            context,
        )
    create_file_from_template(
        env,
        "app/api/v1/__init__.py.jinja",
        os.path.join(project_dir, "app/api/v1/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/api/v1/roles.py.jinja",
        os.path.join(project_dir, "app/api/v1/roles.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/api/v1/users.py.jinja",
        os.path.join(project_dir, "app/api/v1/users.py"),
        context,
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "app/api/v1/auth.py.jinja",
            os.path.join(project_dir, "app/api/v1/auth.py"),
            context,
        )
    create_file_from_template(
        env,
        "app/api/__init__.py.jinja",
        os.path.join(project_dir, "app/api/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/api/router.py.jinja",
        os.path.join(project_dir, "app/api/router.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/__init__.py.jinja",
        os.path.join(project_dir, "app/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/common/__init__.py.jinja",
        os.path.join(project_dir, "app/common/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/integrations/__init__.py.jinja",
        os.path.join(project_dir, "app/integrations/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/tasks/__init__.py.jinja",
        os.path.join(project_dir, "app/tasks/__init__.py"),
        {},
    )
    create_file_from_template(
        env,
        "app/migrations/README.md.jinja",
        os.path.join(project_dir, "app/migrations/README.md"),
        {},
    )


def create_auth_files(project_dir, env, context):
    """Generate authentication and authorization files."""
    create_file_from_template(
        env,
        "app/dependencies/__init__.py.jinja",
        os.path.join(project_dir, "app/dependencies/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/middlewares/__init__.py.jinja",
        os.path.join(project_dir, "app/middlewares/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/security/__init__.py.jinja",
        os.path.join(project_dir, "app/security/__init__.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/middlewares/auth.py.jinja",
        os.path.join(project_dir, "app/middlewares/auth.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/dependencies/auth.py.jinja",
        os.path.join(project_dir, "app/dependencies/auth.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/dependencies/authorization.py.jinja",
        os.path.join(project_dir, "app/dependencies/authorization.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/security/jwt.py.jinja",
        os.path.join(project_dir, "app/security/jwt.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/security/password.py.jinja",
        os.path.join(project_dir, "app/security/password.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/seeds/initial_admin_seeder.py.jinja",
        os.path.join(project_dir, "app/seeds/initial_admin_seeder.py"),
        context,
    )


def create_email_files(project_dir, env, context):
    """Generate email service and schema files."""
    create_file_from_template(
        env,
        "app/services/email.py.jinja",
        os.path.join(project_dir, "app/services/email.py"),
        context,
    )
    create_file_from_template(
        env,
        "app/schemas/email.py.jinja",
        os.path.join(project_dir, "app/schemas/email.py"),
        context,
    )


def create_test_files(project_dir, env, context):
    """Generate pytest scaffold files."""
    create_file_from_template(
        env,
        "tests/conftest.py.jinja",
        os.path.join(project_dir, "tests/conftest.py"),
        context,
    )
    create_file_from_template(
        env,
        "tests/test_health.py.jinja",
        os.path.join(project_dir, "tests/test_health.py"),
        context,
    )
    create_file_from_template(
        env,
        "tests/api/test_users.py.jinja",
        os.path.join(project_dir, "tests/api/test_users.py"),
        context,
    )
    create_file_from_template(
        env,
        "tests/services/test_users_service.py.jinja",
        os.path.join(project_dir, "tests/services/test_users_service.py"),
        context,
    )
    if context.get("with_auth"):
        create_file_from_template(
            env,
            "tests/api/test_auth.py.jinja",
            os.path.join(project_dir, "tests/api/test_auth.py"),
            context,
        )
