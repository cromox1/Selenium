# plusNet Firewall

## SELENIUM

Automation Framework directories:

1) base
2) configfiles
3) pages
4) tests
5) utilities
6) screenshots (create by code automatically)

To run tests (example) :

* py.test -s -v tests/home/login_tests.py --browser firefox --password "xxPSWDxx"

(all tests in 'tests' directory -- to run one by one)

To run specific test from main test set :

* py.test.exe -v -s tests/home/login_tests.py::LoginTests::test_FirewallSettingBlock
* py.test.exe -v -s tests/home/login_tests.py::LoginTests::test_FirewallSettingOff

To run all tests as a test suite :

* py.test tests/test_suite_plusNetFirewall.py     
* py.test -v tests/test_suite_plusNetFirewall.py 

DEFAULT values (if didn't supply) :

'--browser' = firefox

'--password' = (randomly choosen for you from my list)
