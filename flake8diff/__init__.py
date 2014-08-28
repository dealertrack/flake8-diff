from __future__ import unicode_literals, print_function
import argparse
import operator
import os
import six
import sys

from .main import Flake8Diff, COLORS
from .vcs import SUPPORTED_VCS


ENVIRON_PREFIX = 'FLAKE8DIFF_{}'

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
    dest='flake8_options',
    metavar='<options>',
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
         'determine automatically. Can be any of "{}"'
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
    action='store_true',
    default=False,
    help='Be verbose. '
         'This will print out every compared file.',
)
parser.add_argument(
    '--debug',
    action='store_true',
    default=False,
    help='Be even more verbose. '
         'This will print out all debug logs.',
)
default_color = os.environ.get(ENVIRON_PREFIX.format('COLOR'), 'nocolor')
parser.add_argument(
    '--color',
    choices=COLORS.keys(),
    default=default_color,
    type=six.text_type,
    help='Color theme to use. Default is "{}". '
         'Can be any of "{}"'
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
        'verbose': args.verbose,
        'debug': args.debug,
        'color_theme': args.color,
    }

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
