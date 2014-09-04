.. flake8-diff documentation master file, created by
   sphinx-quickstart on Thu Sep  4 11:16:53 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the flake8-diff documentation!
=========================================

Release v\ |release|.


What is this?
=============

flake8-diff is a utility that executes flake8 over a set of files changed
between two VCS versions, and prints out only the violations introduced by the
newer version.  We use this at Dealertrack as part of our code review process,
to show what flake8 violations would be introduced by merging a branch or pull
request.


Installation
============

.. code-block:: bash

    $ pip install flake8-diff

Or to install the latest development version:

.. code-block:: bash

    $ pip install git+git://github.com/dealertrack/flake8-diff


Documentation
=============

.. toctree::
   :maxdepth: 2

   usage


API documentation
-----------------

.. toctree::
   :maxdepth: 2

   api


Contributing
============

.. toctree::
   :maxdepth: 2

   contributing
   development-process

