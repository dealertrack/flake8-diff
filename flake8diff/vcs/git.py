from __future__ import unicode_literals, print_function

from ..utils import _execute
from .base import VCSBase


class GitVCS(VCSBase):
    """
    Git support implementation
    """
    name = 'git'

    def get_vcs(self):
        """
        Get git binary executable path
        """
        return _execute('which git', strict=True).strip()

    def is_used(self):
        """
        Determines if this VCS should be used

        TODO: implement
        """
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
        return _execute(' '.join(cmd), self.logger).split()

    def changed_files(self):
        """
        Return a list of all changed files.
        """
        command = filter(None, [
            self.vcs,
            "diff",
            "--name-only",
        ] + self.commits)

        return filter(self.filter_file,
                      iter(_execute(' '.join(command), self.logger)
                           .splitlines()))
