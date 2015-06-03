from __future__ import unicode_literals, print_function

import logging
import subprocess

from ..utils import _execute
from .base import VCSBase


logger = logging.getLogger(__name__)


class HgVCS(VCSBase):
    """
    Mercurial support implementation
    """
    name = 'hg'

    def get_vcs(self):
        """
        Get git binary executable path
        """
        vcs = _execute('which hg', strict=True).strip()
        return vcs

    def is_used(self):
        """
        Determines if this VCS should be used
        """
        try:
            self._check_mercurial_repository()
        except subprocess.CalledProcessError:
            return False
        return True

    def changed_lines(self, filename):
        """
        Get a list of all lines changed by this set of commits.
        """
        commits = ['-r {}'.format(c) for c in self.commits]

        command_arguments = [
            "--program=diff",
            "'--option=--new-line-format=\"%dn \"'",
            "'--option=--unchanged-line-format=\"\"'",
            "'--option=--changed-group-format=\"%>\"'",
            filename
        ]
        command = [self.vcs, 'extdiff'] + commits + command_arguments
        result = _execute(' '.join(command))

        # Fixes few compatibility issues
        result = result.replace('"', '').strip().split(' ')

        return result

    def changed_files(self):
        """
        Return a list of all changed files.
        """
        commits = ['-r {}'.format(c) for c in self.commits]
        command = [self.vcs, 'diff', '--stat'] + commits
        result = _execute(' '.join(command))
        lines = result.strip().split('\n')[:-1]
        files = [
            line.split('|')[0].strip()
            for line in lines
        ]
        return files

    def check(self):
        try:
            _execute(
                '{vcs} extdiff'.format(vcs=self.vcs), strict=True,
                log_errors=False)
        except subprocess.CalledProcessError:
            message = (
                "Mercurial 'extdiff' extension is disabled.\n"
                "Please add the following lines to your ~/.hgrc\n\n"
                "[extensions]\n"
                "extdiff = \n")
            print(message)
            raise Exception("Please enable 'extdiff' extension")
        return True

    def _check_mercurial_repository(self):
        return _execute(
            '{vcs} status'.format(vcs=self.vcs), strict=True, log_errors=False)
