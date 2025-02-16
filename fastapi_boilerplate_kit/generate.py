"""
The file have generation code for the boilerplate
"""

# pylint: disable=C0116

import os
from jinja2 import Environment, PackageLoader


def generate_project(project_name):
    project_dir = project_name

    # Set up the Jinja environment
    env = Environment(loader=PackageLoader('fastapi_boilerplate_kit', 'templates'))

    # Create directory structure
    create_directories(project_dir)

    # Generate FastAPI app entry point (main.py)
    create_file_from_template(
        env,
        "main.py.jinja",
        os.path.join(project_dir, "main.py"),
        {"project_name": project_name}
    )

    # Generate environment variables
    generate_env(project_dir, env)

    # Generate basic files
    create_basic_files(project_dir, env)

    # Generate core files
    create_core_files(project_dir, env)

    # Generate db files
    create_db_files(project_dir, env)

    # Generate API files
    create_api_files(project_dir, env)

    # Generate utils files
    create_utils_files(project_dir, env)

    print(
        f"Successfully generated the FastAPI boilerplate template to your project - {project_dir}"
    )


def create_directories(base_path):
    dirs = [
        "app",
        "app/api/v1",
        "app/core",
        "app/database",
        "app/models",
        "app/repositories",
        "app/schemas",
        "app/seeds",
        "app/services",
        "utils",
        "utils/global_handlers",
    ]
    for dir_ in dirs:
        os.makedirs(os.path.join(base_path, dir_), exist_ok=True)


def create_file(file_path, content):
    """Helper function to create a file and write content"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        f.write("\n")


def create_file_from_template(env, template_name, file_path, context):
    """Render a Jinja template and create a file"""
    template = env.get_template(template_name)
    rendered_content = template.render(context)
    create_file(file_path, rendered_content)


def generate_env(project_dir, env, db_config='sqlite'):
    """Generate .env configuration"""
    create_file_from_template(
        env,
        ".env.jinja",
        os.path.join(project_dir, ".env"),
        {"db_config": db_config}
    )


def create_basic_files(project_dir, env):
    """Generate basic files for the project"""
    # requirements.txt
    create_file_from_template(
        env,
        "requirements.txt.jinja",
        os.path.join(project_dir, "requirements.txt"),
        {}
    )

    # README.md
    create_file_from_template(
        env,
        "README.md.jinja",
        os.path.join(project_dir, "README.md"),
        {"project_name": project_dir}
    )

    # .pylintrc
    create_file_from_template(
        env, ".pylintrc.jinja", os.path.join(project_dir, ".pylintrc"), {}
    )

    # .gitignore
    create_file_from_template(
        env, ".gitignore.jinja", os.path.join(project_dir, ".gitignore"), {}
    )

    # __init__.py
    create_file_from_template(
        env, "__init__.py.jinja", os.path.join(project_dir, "__init__.py"), {}
    )


def create_utils_files(project_dir, env):
    """Generate utils files"""
    create_file_from_template(
        env,
        "utils/global_handlers/error_handler.py.jinja",
        os.path.join(project_dir, "utils/global_handlers/error_handler.py"),
        {}
    )


def create_db_files(project_dir, env, db_config='sqlite'):
    """Generate database files"""
    create_file_from_template(
        env,
        "app/database/__init__.py.jinja",
        os.path.join(project_dir, "app/database/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/database/config.py.jinja",
        os.path.join(project_dir, "app/database/config.py"),
        {"db_config": db_config}
    )
    create_file_from_template(
        env,
        "app/database/database.py.jinja",
        os.path.join(project_dir, "app/database/database.py"),
        {"db_config": db_config}
    )


def create_core_files(project_dir, env):
    """Generate core files"""
    create_file_from_template(
        env,
        "app/core/__init__.py.jinja",
        os.path.join(project_dir, "app/core/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/core/config.py.jinja",
        os.path.join(project_dir, "app/core/config.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/core/constants.py.jinja",
        os.path.join(project_dir, "app/core/constants.py"),
        {}
    )


def create_api_files(project_dir, env):
    """Generate API routes, services, repositories, schemas and models files"""
    # models
    create_file_from_template(
        env,
        "app/models/__init__.py.jinja",
        os.path.join(project_dir, "app/models/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/models/base_model.py.jinja",
        os.path.join(project_dir, "app/models/base_model.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/models/roles.py.jinja",
        os.path.join(project_dir, "app/models/roles.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/models/users.py.jinja",
        os.path.join(project_dir, "app/models/users.py"),
        {}
    )

    # repositories
    create_file_from_template(
        env,
        "app/repositories/__init__.py.jinja",
        os.path.join(project_dir, "app/repositories/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/repositories/roles.py.jinja",
        os.path.join(project_dir, "app/repositories/roles.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/repositories/users.py.jinja",
        os.path.join(project_dir, "app/repositories/users.py"),
        {}
    )

    # schemas
    create_file_from_template(
        env,
        "app/schemas/__init__.py.jinja",
        os.path.join(project_dir, "app/schemas/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/roles.py.jinja",
        os.path.join(project_dir, "app/schemas/roles.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/users.py.jinja",
        os.path.join(project_dir, "app/schemas/users.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/commons/__init__.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/commons/base_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/base_response.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/commons/role_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/role_response.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/schemas/commons/user_response.py.jinja",
        os.path.join(project_dir, "app/schemas/commons/user_response.py"),
        {}
    )

    # seeds
    create_file_from_template(
        env,
        "app/seeds/__init__.py.jinja",
        os.path.join(project_dir, "app/seeds/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/seeds/roles_seeder.py.jinja",
        os.path.join(project_dir, "app/seeds/roles_seeder.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/seeds/users_seeder.py.jinja",
        os.path.join(project_dir, "app/seeds/users_seeder.py"),
        {}
    )

    # services
    create_file_from_template(
        env,
        "app/services/__init__.py.jinja",
        os.path.join(project_dir, "app/services/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/services/roles.py.jinja",
        os.path.join(project_dir, "app/services/roles.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/services/users.py.jinja",
        os.path.join(project_dir, "app/services/users.py"),
        {}
    )

    # routes
    create_file_from_template(
        env,
        "app/api/v1/__init__.py.jinja",
        os.path.join(project_dir, "app/api/v1/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/api/v1/roles.py.jinja",
        os.path.join(project_dir, "app/api/v1/roles.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/api/v1/users.py.jinja",
        os.path.join(project_dir, "app/api/v1/users.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/api/__init__.py.jinja",
        os.path.join(project_dir, "app/api/__init__.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/api/router.py.jinja",
        os.path.join(project_dir, "app/api/router.py"),
        {}
    )
    create_file_from_template(
        env,
        "app/__init__.py.jinja",
        os.path.join(project_dir, "app/__init__.py"),
        {}
    )
