# GMAIL

## SELENIUM

### Automation Framework directories: ###

1) base
2) configfiles
3) pages
4) tests
5) utilities
6) screenshots (create by code automatically)

### To run tests (example) : ###

* py.test -s -v tests/home/login_tests.py --browser firefox --usrpswd "cromox@gmx.com, Serverg0d!"
* py.test -s -v tests/youtube/youtube_tests.py --browser firefox --usrpswd "cromox@gmx.com, Serverg0d!"
* py.test -s -v tests/googleplay/googleplay_tests.py --browser firefox --usrpswd "cromox@gmx.com, Serverg0d!"
* py.test -v -s tests/googleHangouts/hangouts_tests.py
* py.test -v -s tests/googleNews/googlenews_tests.py

(all tests in 'tests' directory -- to run one by one)

### To run all tests as a test suite : ###

* py.test tests/test_suite_GMAIL.py 
* py.test -v tests/test_suite_GMAIL.py 

**DEFAULT** values (if didn't supply) :

'--browser' = firefox

'--usrpswd' = (randomly choosen for you from my list)
