from __future__ import unicode_literals, print_function

import six


@six.python_2_unicode_compatible
class BaseError(Exception):
    def __str__(self):
        return self.message


class Flake8NotInstalledError(BaseError):
    """
    Exception when run_flake8 installation cannot be found.
    """
    message = ('flake8 installation could not be found. '
               'Is it on $PATH?')


class NotLocatableVCSError(BaseError):
    """
    Exceptions for when VCS cannot be determined automatically
    """
    message = 'VCS could not be determined automatically'


class UnsupportedVCSError(BaseError):
    """
    Exception for handling unknown VCS
    """

    def __init__(self, vcs=None):
        msg = '{0} VCS is not unsupported'
        self.message = msg.format(vcs)
        super(UnsupportedVCSError, self).__init__()


class VCSNotInstalledError(BaseError):
    """
    Exception for when particular vcs installation
    cannot be found.
    """

    def __init__(self, vcs=None):
        msg = ('VCS "{0}" installation could not be found. '
               'Is it on $PATH?')
        self.message = msg.format(vcs)
        super(VCSNotInstalledError, self).__init__()


class WrongVCSSpecified(BaseError):
    """
    Exception for when particular vcs installation
    cannot be found.
    """

    def __init__(self, vcs=None):
        self.message = 'This is not a "{0}" repository'.format(vcs or '')
        super(WrongVCSSpecified, self).__init__()
