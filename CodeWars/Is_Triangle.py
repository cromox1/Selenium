'''
## https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built
with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

'''

__author__ = 'cromox'

# from test.completion.isinstance import Test
# from numpy import test

from nose.tools import assert_equals

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a >= b+c or b >= a+c or c >= a+b:
        return False
    else:
        return True

def test_assert_equals(ii, pp, message):
    try:
        assert_equals(ii, pp, message)
        if ii == False:
            message1 = message
        else:
            message1 = 'OK'
        print(' Equal  -> ', ii, " == ", pp, " / " + message1)
    except:
        if ii == False:
            message1 = message
        else:
            message1 = 'OK'
        print('Unequal -> ', ii, " != ", pp, " / " + message1)

# test.describe('is_triangle')
# test.it("works for some examples")
test_assert_equals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
test_assert_equals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
test_assert_equals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
test_assert_equals(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
test_assert_equals(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
test_assert_equals(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
test_assert_equals(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
test_assert_equals(is_triangle(2, 5, 6), False, "didn't work when sides were 2, 5, 1")
test_assert_equals(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
test_assert_equals(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
test_assert_equals(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
test_assert_equals(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
test_assert_equals(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
test_assert_equals(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
test_assert_equals(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")

test_assert_equals(is_triangle(0, 2, 4), False, "Test")
