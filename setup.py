from setuptools import setup, find_packages


setup(
    name = "flake8-diff",
    version = '0.1.0',
    url = "http://dealertrack.github.io",
    author = "Dealertrack Technologies",
    author_email = "gregory.armer@dealertrack.com",
    description = ("Run flake8 across a set of changed files and filter out "
                   "violations occurring only on the lines that were changed."),
    long_description = '\n' + open('README.md').read(),
    include_package_data = True,
    packages = find_packages(),
    package_data = {'flake8-diff': [ 'README.md' ] },
    zip_safe=False,
    install_requires = ['flake8', 'blessings', 'six'],
    entry_points = {
        'console_scripts': [
            'flake8-diff = flake8diff.main:main'
        ]
    },
    dependency_links = []
)
