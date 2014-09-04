"""
Run flake8 across a set of changed files and filter out violations occurring
only on the lines that were changed.

By default it's configured for "git diff master" which is useful for
buildmasters looking at a checked out PR.

To use, dump this in a file somewhere::

    $ pip install flake8-diff
    $ git checkout pr/NNN
    $ git merge origin/master
    $ flake8-diff

"""
import subprocess
import argparse
import logging
import shutil
import sys
import os
import re


# Setup logging
logger = logging.getLogger(__name__)
FORMAT = "%(asctime)-15s %(name)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.ERROR)


# TODO: Handle these not being found in a better way
GIT = subprocess.check_output(["which", "git"]).strip()
FLAKE8 = subprocess.check_output(["which", "flake8"]).strip()


# Regexes
IS_PYTHON = re.compile(r'.*[.]py$')
LINE = re.compile(r'^([^\s]+):([\d]+):[\d]+: ')


def _execute(cmd):
    """ Make executing a command locally a little less painful.
    """
    logging.debug("executing {}".format(cmd))
    process = subprocess.Popen(cmd.split(' '),
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate()
    returncode = proc.wait()
    if returncode != 0:
        logging.error(err)
    return out


def changed_lines(filename):
    """ Get a list of all lines changed by this set of commits.

    TODO: Support other SCMs
    """
    diff_command = ['diff',
                    '--new-line-format="%dn "',
                    '--unchanged-line-format=""',
                    '--changed-group-format="%>"']
    difftool_command = ['difftool', '-y', '-x',
                        " ".join(diff_command)]

    cmd = [GIT] + difftool_command + ["origin/master", "--", filename]
    return _execute(cmd).split()


def changed_files():
    """ Return a list of all changed files.

    TODO: Support other SCMs
    """
    command = "{} diff --name-only origin/master".format(GIT)
    for filename in _execute(command).splitlines():
        if IS_PYTHON.match(filename):
            yield filename


def flake8(filename):
    """ Run flake8 on a file.

    TODO: Make excludes configurable.
    """
    command = "{} --ignore=E501 {}".format(FLAKE8, filename)
    return _execute(cmd)


def process():
    """ Perform the magic.
    """
    parser = argparse.ArgumentParser(description=globals().__docstring__)

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='be verbose')

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.INFO)

    for filename in changed_files():
        included_lines = changed_lines(filename)
        logger.info("checking {} lines {}".format(filename,
                                                  ', '.join(included_lines)))

        for violation in flake8(filename).splitlines():
            matches = LINE.match(violation)
            if matches:
                matched_file, matched_line = matches.groups()
                if matched_line in included_lines:
                    print violation
