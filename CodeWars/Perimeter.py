'''
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum
of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed
in the same manner as in the drawing:

#Hint: See Fibonacci sequence

#Ref: http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n)
and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
'''

__author__ = 'cromox'

from nose.tools import assert_equals

def perimeter(n):
    total = 0
    for i in range(1,n+2):
        total += fib(i)
    return 4*total

#def fib(n):
#    if n <= 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fib(n-2) + fib(n-1)


#def fib(n):
#    fibs = {0: 0, 1: 1}
#    if n in fibs:
#        return fibs[n]
#    if n % 2 == 0:
#        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
#        return fibs[n]
#    else:
#        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
#        return fibs[n]

#def fib(n):
#    a, b = 0, 1
#    for i in range(n):
#        a, b = b, a+b
#    return a


#def fib(n):
#    table = [0]*1000
#    if n<=1:
#        return n
#    else:
#        if(table[n-1]==0):
#            table[n-1] = fib(n-1)
#        if(table[n-2]==0):
#            table[n-2] = fib(n-2)
#        table[n] = table[n-1] + table[n-2]
#        return table[n]

#def fib(n):
#    return pow(2 << n, n + 1, (4 << 2*n) - (2 << n) - 1) % (2 << n)

#def mul(a, b):
#    return a[0]*b[1]+a[1]*b[0]+a[0]*b[0], a[0]*b[0]+a[1]*b[1]
#def fib(n):
#    x, r = (1, 0), (0, 1)
#    while n:
#        if n & 1:
#            r = mul(r, x)
#        x = mul(x, x)
#        n >>= 1
#    return r[0]

dicFib = { 0:0 ,1 :1 }
iterations = 0

def fib(a):
    if  (a in dicFib):
        return dicFib[a]
    else :
        global iterations
        fibx = fib(a-2)+fib(a-1)
        dicFib[a] = fibx
        iterations += 1
        return fibx

print("FIB")
print("i=1 / " + str(fib(1)))
print("i=2 / " + str(fib(2)))
print("i=3 / " + str(fib(3)))
print("i=4 / " + str(fib(4)))
print("i=5 / " + str(fib(5)))
print("i=6 / " + str(fib(6)))
print("i=7 / " + str(fib(7)))
print("i=8 / " + str(fib(8)))

print("PERIMETER")
print("i=1 / " + str(perimeter(1)))
print("i=2 / " + str(perimeter(2)))
print("i=3 / " + str(perimeter(3)))
print("i=4 / " + str(perimeter(4)))
print("i=5 / " + str(perimeter(5)))
print("i=6 / " + str(perimeter(6)))
print("i=7 / " + str(perimeter(7)))
print("i=8 / " + str(perimeter(8)))

def test_assert_equals(ii, pp):
    try:
        assert_equals(perimeter(ii), pp)
        print(' Equal  ', ii, " - ", perimeter(ii), " == ", pp)
    except:
        print('Unequal ', ii, " - ", perimeter(ii), " != ", pp)

print("TEST")
test_assert_equals(5, 80)
test_assert_equals(6, 132)
test_assert_equals(7, 216)
test_assert_equals(20, 114624)
test_assert_equals(30, 14098308)
test_assert_equals(100, 6002082144827584333104)
test_assert_equals(200, 4754074245292504185728823487231439662628704)
test_assert_equals(500, 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)
#assert_equals(perimeter(30), 14098308)

#assert_equals(perimeter(5), 80)
#assert_equals(perimeter(6), 132)
#assert_equals(perimeter(7), 216)
#assert_equals(perimeter(20), 114624)
#assert_equals(perimeter(30), 14098308)
## assert_equals(perimeter(100), 6002082144827584333104)