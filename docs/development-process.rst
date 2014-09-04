===================
Development Process
===================

We use a number of tools to manage the code and development of flake8-diff:

    * git is our version control system
    * Github for tracking issues, and handling our code review process
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

    * Add a remote to the upstream project to track changes

        .. code-block:: bash

            $ git remote add -f upstream https://github.com/dealertrack/flake8-diff

    * Check out develop or create a feature branch off develop

        .. code-block:: bash

            $ git checkout -b develop upstream/develop
            $ git push -u origin develop

    * Do your work, commit and push, then open a pull request to upstream on
      the develop branch.

    * Handle any review comments, add more commits and push
