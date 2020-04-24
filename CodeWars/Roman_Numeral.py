__author__ = 'cromox'

from nose.tools import assert_equals

def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    numeral = 0
    decode1 = { "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900 }
    decode2 = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
    for key in decode1.keys():
        if key in roman:
            numeral += decode1[key]
            roman = roman.replace(key, '')
    for vv in roman:
        numeral += decode2[vv]
    return numeral

def test_assert_equals(roman, expected):
    try:
        penombo = solution(roman)
        assert_equals(penombo, expected)
        print('Equal   --> ', roman, " / ", penombo, " == ", expected)
    except:
        print('UNEQUAL --> ', roman, " / ", penombo, " != ", expected)

## TDD
test_assert_equals("CM", 900)
test_assert_equals("IX", 9)
test_assert_equals("XIX", 19)
test_assert_equals("XXI", 21)
test_assert_equals("C", 100)
test_assert_equals("D", 500)
test_assert_equals("MM", 2000)
test_assert_equals("MCMXC", 1990)
test_assert_equals("MMVIII", 2008)
test_assert_equals("MDCLXVI", 1666)
