__author__ = 'cromox'

'''
https://www.codewars.com/kata/create-phone-number/python

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

'''

from nose.tools import assert_equals
# from unittest2.test.test_case import Test

def create_phone_number(n):
    phone = '('
    for i in range(3):
        phone = phone + str(n[i])
    phone = phone + ") "
    for i in range(3,6):
        phone = phone + str(n[i])
    phone = phone + "-"
    for i in range(6,len(n)):
        phone = phone + str(n[i])
    # print(phone)
    return phone



#Test.describe("Basic tests")
#Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
#Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
#Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
#Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
#Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

