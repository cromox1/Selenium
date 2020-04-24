# Selenium

## Motors

### Motors.co.uk – Making car buying, selling and owning easy details

Motors.co.uk is a car search portal that aims to make car buying, selling and owning easy by empowering and enlightening automotive buyers and sellers with smart, intuitive tools.

Motors.co.uk is proud to be owned by Cox Automotive, the world’s largest automotive services company.
Motors.co.uk is authorised and regulated by the Financial Conduct Authority. Full details upon request.
Motors.co.uk Head Office, 127 Olympic Avenue, Milton Park, Abingdon, Oxfordshire, OX14 4SA

E-mail:
sales@motors.co.uk

Visit the site:
www.motors.co.uk

Motors Automation Framework consise these directories:

1) apps
2) base
3) configfiles
4) pages
5) tests
6) utilities
7) screenshots

To run tests (example) :

### py.test -s -v tests/home/login_tests.py --browser firefox

(all tests in 'tests' directory -- to run one by one)

To run all tests as a test suite :

### py.test tests/test_suite_Motors.py --browser firefox 
### py.test -v tests/test_suite_Motors.py --browser firefox

----------------------------------
(Not implemeted yet !!!!!)

New option : --loginusrpswd "tenantname, useremail_tologin, password" 

* py.test tests/test_suite_eCDA.py --browser firefox --loginusrpswd "cromoxgmx, cromox@gmx.com, Serverg0d!"
* py.test -v tests/test_suite_eCDA.py --browser firefox --loginusrpswd "cromoxgmx, cromox@gmx.com, Serverg0d!"

If user didn't suplied the --loginusrpswd options, or the options is in wrong format, it will use DEFAULT one:
* py.test -v tests/test_suite_Motors.py --browser firefox

(the DEFAULT one which will be use - is a random of \[burgessgmx, carlgmx, cromoxgmx\])

