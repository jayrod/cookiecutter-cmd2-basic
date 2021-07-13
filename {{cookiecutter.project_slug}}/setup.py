"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


setup(
    name='{{cookiecutter.project_name}}',

    version='{{cookiecutter.version}}',

    description='{{cookiecutter.project_short_description}}',

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',

    install_requires=['cmd2'],  # Optional

    entry_points={  # Optional
        'console_scripts': [
            '{{cookiecutter.command_name}}={{cookiecutter.project_slug}}:main',
        ],
    },
)
