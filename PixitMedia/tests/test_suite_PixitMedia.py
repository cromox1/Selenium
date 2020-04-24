__author__ = 'cromox'

import unittest
from tests.p01google.p01searchpixitmedia_tests import P01SearchPixitMediaTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(P01SearchPixitMediaTests)
# tc2 - TODO
# tc3 - TODO

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])
# smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
