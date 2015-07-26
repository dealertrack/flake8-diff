from unittest import TestCase

from flake8diff import flake8


class Flake8DiffTestCase(TestCase):
    def test_flake8diff(self):
        flake8.Flake8Diff("", {})
