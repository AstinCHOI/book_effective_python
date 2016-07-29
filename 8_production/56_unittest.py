
from tempfile import TemporaryDirectory
from unittest import TestCase


class MyTest(TestCase):

    def setUp(self):
        self.test_dir = TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()
    # Test methods follow


# unittest.mock for python3 / mock open source package for python2
# unit test / integration test

# other refs
# nose: nose.readthedocs.org
# pytest: pytest.org 