"""This test is primarily to trigger the argparse code in main.py
"""
from unittest import TestCase

from flake8diff import main  # noqa


class MainTestCase(TestCase):
    def test_main(self):
        # using assertTrue() instead of assertIsNotNone() for py2.6 compat
        self.assertTrue(main.LOGGING_FORMAT is not None)
