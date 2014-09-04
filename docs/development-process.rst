===================
Development Process
===================

We use a number of tools to manage the code and development of flake8-diff:

    * git is our version control system
    * Github for tracking issues, and handling our code review process
    * git flow to manage our branches
    * Travis CI to run our tests, and Coveralls to track test coverage
    * Sphinx to handle our documentation


Getting started
===============

To get setup for development you can follow the below steps:

    * Fork the repository from https://github.com/dealertrack/flake8-diff
    * Clone and install requirements:

        .. code-block:: bash

            $ git clone
            $ mkvirtualenv flake8-diff
            $ pip install -r requirements.pip

    * Use git flow to start a new feature branch

        .. code-block:: bash

            $ git flow feature start name-of-feature
            # do work, commit and push, then open a pull request

    * Handle any review comments, add more commits and push
