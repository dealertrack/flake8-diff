"""This test is primarily to trigger the argparse code in main.py
"""
from unittest import TestCase

from flake8diff import main  # noqa


class MainTestCase(TestCase):
    def test_main(self):
        self.assertIsNotNone(main.LOGGING_FORMAT)
