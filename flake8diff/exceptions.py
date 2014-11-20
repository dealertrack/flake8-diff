from __future__ import unicode_literals, print_function


class Flake8NotInstalledError(Exception):
    """
    Exception when run_flake8 installation cannot be found.
    """
    message = ('flake8 installation could not be found. '
               'Is it on $PATH?')


class NotLocatableVCSError(Exception):
    """
    Exceptions for when VCS cannot be determined automatically
    """
    message = 'VCS could not be determined automatically'


class UnsupportedVCSError(Exception):
    """
    Exception for handling unknown VCS
    """

    def __init__(self, vcs=None):
        msg = '{0} VCS is not unsupported'
        self.message = msg.format(vcs)


class VCSNotInstalledError(Exception):
    """
    Exception for when particular vcs installation
    cannot be found.
    """

    def __init__(self, vcs=None):
        msg = ('VCS "{0}" installation could not be found. '
               'Is it on $PATH?')
        self.message = msg.format(vcs)
