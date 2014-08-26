from __future__ import unicode_literals, print_function


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
        msg = '{} VCS is not unsupported'
        self.message = msg.format(vcs)
