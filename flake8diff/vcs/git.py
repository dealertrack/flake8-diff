from __future__ import unicode_literals, print_function
import subprocess

from ..utils import _execute
from .base import VCSBase


# TODO: Handle these not being found in a better way
GIT = subprocess.check_output(["which", "git"]).strip()


class GitVCS(VCSBase):
    """
    Git support implementation
    """
    name = 'git'

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
            GIT,
            'difftool',
            '-y',
            '-x',
            "'{}'".format(' '.join(diff_command)),
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
            GIT,
            "diff",
            "--name-only",
        ] + self.commits)

        return filter(self.filter_file,
                      iter(_execute(' '.join(command), self.logger)
                           .splitlines()))
