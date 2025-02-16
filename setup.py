"""
The file have setup code for the boilerplate
"""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fastapi_boilerplate_kit',
    version='1.5.8',
    packages=find_packages(),
    python_requires='>=3.10',
    package_data={
        'fastapi_boilerplate_kit': ['templates/*.jinja'],
    },
    include_package_data=True,
    py_modules=['cli'],
    install_requires=[
        'Click',
        'jinja2',
    ],
    entry_points='''
        [console_scripts]
        dnd=fastapi_boilerplate_kit.cli:cli
    ''',
    author='Tharunkumar Saravanan',
    author_email='tharunkumar.developers@gmail.com',
    description='A boilerplate for FastAPI projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Tharunkumar2024/fastapi-boilerplate-kit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache 2.0',
)
