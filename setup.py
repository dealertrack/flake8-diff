from setuptools import setup, find_packages
import flake8diff


def read(path):
    with open(path, 'rb') as fid:
        return fid.read().decode('utf-8')


setup(
    name="flake8-diff",
    version=flake8diff.__version__,
    url="http://dealertrack.github.io",
    author="Dealertrack Technologies",
    author_email="gregory.armer@dealertrack.com",
    description=flake8diff.__description__,
    long_description='\n' + read('README.rst'),
    download_url=(
        'https://github.com/dealertrack/flake8-diff/releases/tag/v'
        + flake8diff.__version__
    ),
    include_package_data=True,
    packages=find_packages(),
    package_data={'flake8-diff': ['README.rst']},
    zip_safe=False,
    install_requires=[
        'flake8',
        'argparse',
        'blessings',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'flake8-diff=flake8diff.main:main'
        ]
    },
    dependency_links=[]
)
