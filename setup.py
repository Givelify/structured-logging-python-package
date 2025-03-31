from setuptools import find_packages, setup

setup(
    name='givelifylogging',
    packages=find_packages(),
    version='0.1.0',
    description='Givelify Structured logging library',
    author='Me',
    install_requires=['python-json-logger==2.0.2'],
    setup_requires=['pytest-runner'],
    extras_require={  # Optional
        "dev": ["check-manifest"],
        "test": ['pytest==4.4.1'],
    },
)