'''
####
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
####
'''

__author__ = 'cromox'

from nose.tools import assert_equals

def make_readable(seconds):
    sec = seconds - 60*int(seconds/60)
    min = int(seconds/60) - 60*int(seconds/(60*60))
    hrs = int(seconds/(60*60))
    time = inttostring(hrs)+":"+inttostring(min)+":"+inttostring(sec)
    return time

def inttostring(int):
    if int < 10:
        string = "0" + str(int)
    else:
        string = str(int)
    return string

### TDD

def Test_assert_equals(seconds, expected):
    try:
        readabletime = make_readable(seconds)
        assert_equals(readabletime, expected)
        print('Equal   --> ', seconds, " / ", readabletime, " == ", expected)
    except:
        print('UNEQUAL --> ', seconds, " / ", readabletime, " != ", expected)

Test_assert_equals(0, "00:00:00")
Test_assert_equals(5, "00:00:05")
Test_assert_equals(60, "00:01:00")
Test_assert_equals(3661, "01:01:01")
Test_assert_equals(3749, "01:02:29")
Test_assert_equals(86399, "23:59:59")
Test_assert_equals(359999, "99:59:59")
Test_assert_equals(759999, "211:06:39")
