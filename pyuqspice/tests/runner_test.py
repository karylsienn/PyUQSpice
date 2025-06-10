import unittest
from pyuqspice.ltspicer.runners import LTSpiceRunner

class RunTests(unittest.TestCase):

    @unittest.skip("Skip for building.")
    def test_running_asc(self):
        ltrunner = LTSpiceRunner()
        self.assertTrue(ltrunner.run("pyuqspice/test_files/Transient/simple_resistor_ver2.asc"))
