__author__ = 'cromox'

'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

from nose.tools import assert_equals

#def scramble(s1, s2):
#    result = ""
#    for vv in s2:
#        if s1.count(vv) >= s2.count(vv):
#            result += "1"
#        else:
#            result += "0"
#    # print(result)
#    if "0" in result:
#        return False
#    else:
#        return True

#def scramble(s1, s2):
#    result = ""
#    ls1 = len(s1)
#    ls2 = len(s2)
#    for vv in s2:
#        s3 = s1.replace(vv, "")
#        s4 = s2.replace(vv, "")
#        if ls1 - len(s3) >= ls2 - len(s4):
#            result += "1"
#        else:
#            result += "0"
#    if "0" in result:
#        return False
#    else:
#        return True

#def scramble(s1, s2):
#    result = ""
#    for vv in s2:
#        s1count = 0
#        s2count = 0
#        for i in s2:
#            if i == vv:
#                s2count += 1
#        for i in s1:
#            if i == vv:
#                s1count += 1
#        if s1count >= s2count:
#            result += "1"
#        else:
#            result += "0"
#    # print(result)
#    if "0" in result:
#        return False
#    else:
#        return True

def scramble(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    print(s1)
    print(s2)
    result = ""
    if "0" in result:
        return False
    else:
        return True

### TDD

def Test_assert_equals(wordxx, wordx, expected):
    try:
        whatget = scramble(wordxx, wordx)
        assert_equals(whatget, expected)
        print('Equal   --> ', wordxx, " / ", wordx, " / ", whatget, " == ", expected)
    except:
        print('UNEQUAL --> ', wordxx, " / ", wordx, " / ", whatget, " != ", expected)

#Test.assert_equals(scramble('rkqodlw', 'world'),  True)
#Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
#Test.assert_equals(scramble('katas', 'steak'), False)
#Test.assert_equals(scramble('scriptjava', 'javascript'), True)
#Test.assert_equals(scramble('scriptingjava', 'javascript'), True)

Test_assert_equals('rkqodlw', 'world',  True)
Test_assert_equals('cedewaraaossoqqyt', 'codewars', True)
#Test_assert_equals('katas', 'steak', False)
#Test_assert_equals('kata', 'kkaa', False)
#Test_assert_equals('scriptjava', 'javascript', True)
#Test_assert_equals('scriptingjava', 'javascript', True)
#Test_assert_equals('scriptingjava', 'javascriptx', False)
