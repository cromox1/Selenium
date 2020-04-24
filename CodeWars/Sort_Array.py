__author__ = 'cromox'

from nose.tools import assert_equals

def sort_array(source_array):
    # Return a sorted array.
    sorted_array = source_array
    tmplist = []
    tmpi = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            tmpi.append(i)
            tmplist.append(source_array[i])
    tmplist.sort()
    j = 0
    for i in tmpi:
        sorted_array[i] = tmplist[j]
        j += 1
    return sorted_array

assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
assert_equals(sort_array([]),[])