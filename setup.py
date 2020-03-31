from setuptools import setup, find_packages

INSTALL_REQUIREMENTS = [
    "requests",
]

TEST_REQUIREMENTS = [
    "black",
    "pylint",
]
# black is listed so that contributors can conform to the same code style
# pylint is listed so that contributors can perform static code analysis

setup(
    name="show-open-food-trucks",
    packages=find_packages(),
    include_package_data=True,
    keywords="show food trucks open now",
    url="",
    license="",
    author="",
    author_email="",
    description="A command-line-application "
    "to print out all food open food trucks in San Francisco.",
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={"tests": TEST_REQUIREMENTS},
    entry_points={"console_scripts": ["show-open-food-trucks=src.main:main"]},
    version="1.0",
)
