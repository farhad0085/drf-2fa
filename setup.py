import pathlib
from setuptools import setup

# The directory containing this file
BASE_PATH = pathlib.Path(__file__).resolve().parent

# The text of the README file
README = (BASE_PATH / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="drf-2fa",
    version="1.0.0",
    description="Integrate 2 Factor Authentication in Your Django REST API project easily.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/farhad0085/drf-2fa",
    author="Farhad Hossain",
    author_email="farhadhossain0085@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["drf_2fa", "drf_2fa/migrations", "drf_2fa/backends"],
    package_data={'drf_2fa': ['templates/**/**/*.*']},
    include_package_data=True,
    install_requires=[],
)

# build
# python setup.py sdist bdist_wheel
# upload to pypi
# twine upload dist/*