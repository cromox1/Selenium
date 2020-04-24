__author__ = 'cromox'

import unittest
from tests.home.login_tests import LoginTests
from tests.youtube.youtube_tests import YoutubeTests
from tests.googleplay.googleplay_tests import PlayGoogleTests
from tests.googleHangouts.hangouts_tests import HangOutsTests
from tests.googleNews.googlenews_tests import NewsTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(YoutubeTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PlayGoogleTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(HangOutsTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(NewsTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
