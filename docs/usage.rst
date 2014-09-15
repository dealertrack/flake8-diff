.. py:currentmodule:: flake8diff

=================
Using flake8-diff
=================

The most simple usage of flake8-diff is to run flake8-diff on its own:

.. code-block:: bash

    $ flake8-diff


Basic usage
===========

There are a number of basic parameters you can pass to flake8-diff, and
explanation of these options is below:

.. code-block:: bash

    $ flake8-diff -h


Managing output
===============

TODO: Update once decisions on output, formatting and colors is settled.


Controlling comparisons
=======================

By default flake8-diff will compare your current branch to the equivalent of
origin/master (this is different in other version control systems).

If you want to do the comparison against different branches, or even different
commits, then you can follow the below options.

