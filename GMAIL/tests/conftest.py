__author__ = 'cromox'

import pytest
import sys
from base.webdriverfactory import WebDriverFactory as webbrowser
import datetime
import time
import os
import random

@pytest.yield_fixture()
def setUp():
    print("\n--- > Running method level setUp")
    yield
    print("\n--- > Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, usrpswd):
    print("\n== > Running one time setUp")
    print('Python Version = ' + sys.version)

    masani = datetime.datetime.now().strftime("%Y%m%d")
    userpswdone = gmailUserPassword(usrpswd)
    usrpswd = str(userpswdone[0]+','+userpswdone[1]+',')
    userPasswordWrite("USRPSWD#" + usrpswd + '\n', masani)

    wdf = webbrowser(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield

    print("\n== > Running one time tearDown")
    removeTempFile(masani)

    ### Last sekali... LOGOUT
    time.sleep(1)
    gmaillogout = "https://accounts.google.com/Logout"
    driver.get(gmaillogout)
    time.sleep(1)
    # driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--usrpswd", help="GMAIL 'user,pswd'")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def usrpswd(request):
    return request.config.getoption("--usrpswd")

### gmailuser & password extraction

def gmailUserPassword(usrpswd=""):
    if usrpswd is not None and len(usrpswd.replace(' ','').split(',')) > 1:
        print("\nusrpswd OK = " + usrpswd)
    else:                
        print("\nusrpswd given WAS NOT OK ( " + str(usrpswd) + " )")
        ## Sample tests users' accounts - to randomly choose and use
        a3 = 'user1, Password5!'
        a4 = 'user2, Password4!'
        a5 = 'user3, Password3!'
        a6 = 'user4@gmail.com, Password2!'
        a7 = 'user5@yahoo.co.uk, Password1!'
        usrpswd = random.sample([a3, a4, a5, a6, a7],2)[-1]
        print("Switch to DEFAULT usrpswd ( " + usrpswd + " )")

    if len(usrpswd.replace(' ','').split(',')[0].split('@')) == 2:
        gmailuser = usrpswd.replace(' ','').split(',')[0]
    elif len(usrpswd.replace(' ','').split(',')[0].split('@')) == 1:
        gmailuser = usrpswd.replace(' ','').split(',')[0] + '@gmail.com'
    else:
        # gmailuser = None
        print("\nWRONG USER PASSWORD GIVEN !!!\n")
        return
    gmailpswd = usrpswd.replace(' ','').split(',')[1]

    return gmailuser,gmailpswd

### "--tntusrpswd" options input data put to temp file

def userPasswordWrite(inputdata, timewrite):
    newfile = open('tmp_gmailuserpswd_' + str(timewrite) + '.txt', 'a')
    newfile.write(inputdata)
    newfile.close()

def userPasswordRead(wordmatch, timewrite):
    linematch = []
    for line in open('tmp_gmailuserpswd_' + str(timewrite) + '.txt', 'r'):
        if wordmatch in line:
            linematch.append(line)
    return linematch[-1].split(wordmatch)[1]


def removeTempFile(timewrite):
    newfile = 'tmp_gmailuserpswd_' + str(timewrite) + '.txt'
    os.remove(newfile)
