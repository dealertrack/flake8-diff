from __future__ import unicode_literals

from unittest import TestCase

from flake8diff.exceptions import (
    Flake8NotInstalledError,
    NotLocatableVCSError,
    UnsupportedVCSError,
    VCSNotInstalledError,
    WrongVCSSpecified
)


class ExceptionsTestCase(TestCase):
    def test_flake8_not_installed(self):
        expected = "flake8 installation could not be found. Is it on $PATH?"

        try:
            raise Flake8NotInstalledError
        except Flake8NotInstalledError as e:
            self.assertEqual(str(e), expected)

    def test_not_locatable_vcs(self):
        expected = "VCS could not be determined automatically"

        try:
            raise NotLocatableVCSError
        except NotLocatableVCSError as e:
            self.assertEqual(str(e), expected)

    def test_unsupported_vcs(self):
        expected = "foo VCS is not supported"

        try:
            raise UnsupportedVCSError(vcs="foo")
        except UnsupportedVCSError as e:
            self.assertEqual(str(e), expected)

    def test_vcs_not_installed(self):
        expected = 'VCS "bar" installation could not be found. Is it on $PATH?'

        try:
            raise VCSNotInstalledError(vcs="bar")
        except VCSNotInstalledError as e:
            self.assertEqual(str(e), expected)

    def test_wrong_vcs_specified(self):
        expected = 'This is not a "baz" repository'

        try:
            raise WrongVCSSpecified(vcs="baz")
        except WrongVCSSpecified as e:
            self.assertEqual(str(e), expected)
