# FastAPI Boilerplate Kit

This is a FastAPI Boilerplate Kit to generate the basic configurations to start development and deployment-ready templates.

## Features:
- **FastAPI Boilerplate**: A simple and clean project setup for creating FastAPI applications.
- **Pre-configured Templates**: Includes templates for essential files such as `main.py`, `Dockerfile`, `requirements.txt`, and others.
- **Command-Line Interface (CLI)**: Generate a new FastAPI project with a single command.
- **Production-Ready Setup**: Provides a basic structure that is ready for deployment.

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
Once the installation is complete, you can generate a new FastAPI project using the CLI:

```
dnd generate PROJECT_NAME
```

This will create a new project directory named `PROJECT_NAME` with the default structure for a FastAPI project.

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

### Commands
* `dnd generate PROJECT_NAME`: Generate a new FastAPI project with the specified `PROJECT_NAME`.

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

## Known Issues:
* None at the moment (first release).

## Future Improvements:
* Add user authentication/authorization templates.
* Docker integration for deploying FastAPI applications.

## License:
This project is licensed under the Apache License - see the [LICENSE](https://github.com/Tharunkumar2024/fastapi-boilerplate-kit/blob/main/LICENSE) file for details.

Enjoy building with FastAPI using **DND**, making it easier than ever! 🚀💻
