'''

## https://www.codewars.com/kata/descending-order/python

Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:

Input: 21445 Output: 54421
Input: 145263 Output: 654321
Input: 1254859723 Output: 9875543221

## https://www.codewars.com/kata/descending-order/solutions/python

'''

__author__ = 'cromox'

import unittest2

def Descending_Order(num):
    string1 = str(num)
    len1 = len(string1)
    list1 = []
    for i in range(len1):
        list1.append(int(string1[i]))
    list1.sort(reverse=True)
    string2 = ""
    for i in range(len1):
        string2 = string2 + str(list1[i])
    return int(string2)

    #Bust a move right here

# test.assert_equals(Descending_Order(0), 0)


print(Descending_Order(12344495678))

#test.assert_equals(Descending_Order(15), 51)
#test.assert_equals(Descending_Order(21445), 54421)
#test.assert_equals(Descending_Order(145263), 654321)
#test.assert_equals(Descending_Order(1254859723), 9875543221)
#test.assert_equals(Descending_Order(123456789), 987654321)

# print(Descending_Order(123456789))

### Solutions Orang
#
#def Descending_Order(num):
#    return int("".join(sorted(str(num), reverse=True)))
#
#def Descending_Order(num):
#    s = str(num)
#    s = list(s)
#    s = sorted(s)
#    s = reversed(s)
#    s = ''.join(s)
#    return int(s)
#
#def Descending_Order(num):
#    return int(''.join(sorted(str(num))[::-1]))
#
#def Descending_Order(num):
#    li=[x for x in str(num)]
#    li.sort(reverse=True)
#    return int(''.join(x for x in li))
#
#def Descending_Order(num):
#    x = [i for i in str(num)]
#    x.sort()
#    return int(''.join(x[::-1]))
#
#def Descending_Order(num):
#    print(num);
#    if num==1021:
#        return 2110;
#    return int(str(num)[::-1]);



