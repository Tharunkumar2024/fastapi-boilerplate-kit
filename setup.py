"""
The file have setup code for the boilerplate
"""

from setuptools import setup, find_packages

setup(
    name='fastapi_boilerplate_kit',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fastapi-boilerplate-kit=cli:cli
    ''',
    author='Tharunkumar Saravanan',
    author_email='tharunkumar.developers@gmail.com',
    description='A boilerplate for FastAPI projects',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tharunkumar2024/fastapi-boilerplate-kit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache 2.0',
)
