import sys
import unittest
from subprocess import CalledProcessError

import pytest
import six
from flake8diff import utils


class UtilsTestCase(unittest.TestCase):
    def test_execute_success(self):
        pwd = utils._execute("pwd", strict=True)
        self.assertTrue(pwd is not "")
        self.assertTrue(isinstance(pwd, six.string_types))

    @pytest.mark.skipif(sys.version_info < (2, 7),
                        reason="Python >=2.7 needed")
    def test_execute_failure(self):
        with self.assertRaises(CalledProcessError):
            utils._execute("doesnotexist", strict=True)
