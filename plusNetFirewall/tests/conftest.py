__author__ = 'cromox'

import pytest
import sys
from base.webdriverfactory import WebDriverFactory as webbrowser
import datetime
# import time
import os
# import random

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
    userPasswordWrite("ADMINPSWD#" + adminpswd + '\n', masani)

    wdf = webbrowser(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield

    print("\n== > Running one time tearDown")
    removeTempFile(masani)

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

### "--adminpswd" options input data put to temp file
def userPasswordWrite(inputdata, timewrite):
    newfile = open('tmp_plusnetadminpswd_' + str(timewrite) + '.txt', 'a')
    newfile.write(inputdata)
    newfile.close()

def userPasswordRead(wordmatch, timewrite):
    linematch = []
    for line in open('tmp_plusnetadminpswd_' + str(timewrite) + '.txt', 'r'):
        if wordmatch in line:
            linematch.append(line)
    return linematch[-1].split(wordmatch)[1]

def removeTempFile(timewrite):
    newfile = 'tmp_plusnetadminpswd_' + str(timewrite) + '.txt'
    os.remove(newfile)
