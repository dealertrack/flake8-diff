from __future__ import unicode_literals, print_function
import re

from ..exceptions import VCSNotInstalledError


IS_PYTHON = re.compile(r'.*[.]py$')


class VCSBase(object):
    name = None

    def __init__(self, commits, options, logger):
        self.commits = commits
        self.options = options
        self.logger = logger

        try:
            self.vcs = self.get_vcs()
        except:
            raise VCSNotInstalledError(self.name)

    def get_vcs(self):
        """
        Get the binary executable of the vcs
        """
        raise NotImplementedError

    def is_used(self):
        """
        If this VCS is used
        """
        raise NotImplementedError

    def changed_lines(self, filename):
        """
        Get a list of all lines changed by this set of commits.
        """
        raise NotImplementedError

    def filter_file(self, filename):
        """
        Function which given filename determines
        if the file should be compared
        """
        return IS_PYTHON.match(filename)

    def changed_files(self):
        """
        Return a list of all changed files.
        """
        raise NotImplementedError
