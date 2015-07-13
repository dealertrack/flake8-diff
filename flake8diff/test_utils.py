from unittest import TestCase
import six

from flake8diff import utils
from subprocess import CalledProcessError


class UtilsTestCase(TestCase):
    def test_execute_success(self):
        pwd = utils._execute("pwd", strict=True)
        self.assertIsNotNone(pwd)
        self.assertIsInstance(pwd, six.text_type)

    def test_execute_failure(self):
        with self.assertRaises(CalledProcessError):
            error = utils._execute("doesnotexist", strict=True)
            self.assertEquals(error, "")
