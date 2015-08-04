from __future__ import unicode_literals, print_function

import logging
import subprocess

from ..utils import _execute
from .base import VCSBase


logger = logging.getLogger(__name__)


class GitVCS(VCSBase):
    """
    Git support implementation
    """
    name = 'git'

    def get_vcs(self):
        """
        Get git binary executable path
        """
        return _execute('which git', strict=True, log_errors=False).strip()

    def is_used(self):
        """
        Determines if this VCS should be used
        """
        try:
            self._is_git_repository()
        except subprocess.CalledProcessError:
            return False
        return True

    def changed_lines(self, filename):
        """
        Get a list of all lines changed by this set of commits.
        """
        diff_command = [
            'diff',
            '--new-line-format="%dn "',
            '--unchanged-line-format=""',
            '--changed-group-format="%>"'
        ]
        difftool_command = [
            self.vcs,
            'difftool',
            '-y',
            '-x',
            "'{0}'".format(' '.join(diff_command)),
        ]

        cmd = filter(None, difftool_command + self.commits + [
            "--",
            filename
        ])
        return _execute(' '.join(cmd)).split()

    def changed_files(self):
        """
        Return a list of all changed files.
        """
        command = filter(None, [
            self.vcs,
            "diff",
            "--name-only",
            "--diff-filter=ACMRTUXB",
        ] + self.commits)

        return filter(self.filter_file,
                      iter(_execute(' '.join(command))
                           .splitlines()))

    def _is_git_repository(self):
        return _execute(
            '{vcs} status'.format(vcs=self.vcs), strict=True, log_errors=False)
