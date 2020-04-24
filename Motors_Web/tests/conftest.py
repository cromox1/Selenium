__author__ = 'cromox'

import pytest
import sys
from base.webdriverfactory import WebDriverFactory as webbrowser
import datetime

@pytest.yield_fixture()
def setUp():
    print("\n--- > Running method level setUp")
    yield
    print("\n--- > Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, adminpswd):
    print("\n== > Running one time setUp")
    print('Python Version = ' + sys.version)

    masani = datetime.datetime.now().strftime("%Y%m%d")
    userpswdone = userPassword(adminpswd)
    adminpswd = str(userpswdone + ',')
    # userPasswordWrite("ADMINPSWD#" + adminpswd + '\n', masani)

    wdf = webbrowser(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield

    print("\n== > Running one time tearDown")
    # removeTempFile(masani)

    if driver.name != 'firefox':
        driver.quit()
    #else:
    #    driver.close()

    # display.stop()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--adminpswd", help="Admin Passwd = 'XXadminpswdXX'")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def adminpswd(request):
    return request.config.getoption("--adminpswd")

### admin password extraction
def userPassword(adminpswd=""):
    if adminpswd is not None and len(adminpswd.replace(' ','').split(',')) > 0:
        print("\nadminpswd OK = " + adminpswd)
    else:
        adminpswd = 'M6NXP6FF'
    plusNetPswd = adminpswd.replace(' ','').split(',')[0]
    return plusNetPswd
