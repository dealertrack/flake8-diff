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
from __future__ import unicode_literals, print_function
import argparse
import logging
import operator
import os
import six
import sys

from .flake8 import Flake8Diff, COLORS, logger
from .vcs import SUPPORTED_VCS


ENVIRON_PREFIX = 'FLAKE8DIFF_{0}'
VERBOSITY_MAPPING = {
    0: logging.ERROR,
    1: logging.INFO,
    2: logging.DEBUG,
}


parser = argparse.ArgumentParser(
    description='This script runs flake8 across a set of changed files '
                'and filters out violations occurring only on the lines '
                'that were changed.',
)

parser.add_argument(
    'commit',
    default=['origin/master'],
    nargs='*',
    type=six.text_type,
    help='At most two commit hashes or branch names '
         'which will be compared to figure out '
         'changed lines between the two. '
         'If only one commit is provided, '
         'that commit will be compared against '
         'current files.'
         'Default is "origin/master".',
)
parser.add_argument(
    '--flake8-options',
    default=[],
    dest='flake8_options',
    metavar='<options>',
    nargs=argparse.REMAINDER,
    type=six.text_type,
    help='Options to be passed to flake8 command. '
         'Can be used to configure flake8 on-the-fly when '
         'flake8 configuration file is not present.',
)
parser.add_argument(
    '--vcs',
    choices=map(operator.attrgetter('name'), SUPPORTED_VCS.values()),
    type=six.text_type,
    help='VCS to use. By default VCS is attempted to '
         'determine automatically. Can be any of "{0}"'
         ''.format(', '.join(map(operator.attrgetter('name'),
                                 SUPPORTED_VCS.values()))),
)
parser.add_argument(
    '--standard-flake8-output',
    action='store_true',
    default=False,
    dest='standard_flake8_output',
    help='Output standard flake8 output instead of simplified, '
         'more readable summary.',
)
parser.add_argument(
    '-v', '--verbose',
    action='count',
    default=0,
    help='Be verbose. '
         'This will print out every compared file. '
         'Can be supplied multiple times to increase verbosity level',
)
default_color = os.environ.get(ENVIRON_PREFIX.format('COLOR'), 'off')
parser.add_argument(
    '--color',
    choices=COLORS.keys(),
    default=default_color,
    type=six.text_type,
    help='Color theme to use. Default is "{0}". '
         'Can be any of "{1}"'
         ''.format(default_color,
                   ', '.join(COLORS.keys())),
)


def main():
    args = parser.parse_args()
    if len(args.commit) > 2:
        parser.error('At most 2 commits can be provided.')

    options = {
        'commits': args.commit,
        'vcs': args.vcs,
        'flake8_options': args.flake8_options,
        'standard_flake8_output': args.standard_flake8_output,
        'color_theme': args.color,
    }

    logger.setLevel(VERBOSITY_MAPPING.get(args.verbose, 0))

    any_violations = False
    try:
        any_violations = not Flake8Diff(
            commits=args.commit,
            options=options,
        ).process()
    except Exception as e:
        parser.error(e.message)

    if any_violations:
        sys.exit(1)
