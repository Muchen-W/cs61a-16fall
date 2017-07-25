HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n <= 3:
        return n

    i, g_1, g_2, g_3 = 4, 3, 2, 1
    while i < n:
        g_1, g_2, g_3 = g_1 + 2 * g_2 + 3 * g_3, g_1, g_2
        i += 1
    return g_1 + 2 * g_2 + 3 * g_3
        


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    # solution 2: separate direction decision from value calculation recursively
    def pingpong2(n):
        if n < 7:
            return n
        else:
            return pingpong2(n-1) + direction(n-1)

    def direction(n):
        if n < 7:
            return 1
        elif has_seven(n) or n % 7 == 0:
            return -1 * direction(n-1)
        else:
            return direction(n-1)

    return pingpong2(n)

    # solution 1: starting from 1st and recursively increase to n
    def pingpong_next(k, val, up):
        if k == n:
            return val
        elif up:
            return pingpong_switch(k + 1, val + 1, up)
        else:
            return pingpong_switch(k + 1, val - 1, up)

    def pingpong_switch(k, val, up):
        if has_seven(k) or k % 7 == 0:
            return pingpong_next(k, val, not up)
        else:
            return pingpong_next(k, val, up)

    return pingpong_next(1, 1, True)

    # rudimentary solution
    def cal(n):
        def sign(delta):
            if has_seven(n) or n % 7 == 0:                
                return -1 * delta
            return delta

        if n == 1:
            return 1, sign(1)
        else:
            return sum(cal(n - 1)), sign(cal(n-1)[1])
    return cal(n)[0]

    #i, num, delta = 1, 0, 1
    #while i <= n:
    #    num += delta
    #    if has_seven(i) or i % 7 == 0:
    #        delta *= -1
    #    i += 1
    #return num

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    from math import log2
    lst = [2**i for i in range(int(log2(amount))+1)]
    return counter(amount)
    return counter1(amount, lst)
    return counter2(amount, lst)

def counter(amount, min_coin=1):
    if amount == 0:
        return 1
    elif amount < min_coin:
        return 0
    else:
        return counter(amount-min_coin, min_coin) + counter(amount, 2*min_coin)

def counter1(amount, lst):
    if amount < 0 or not lst:
        return 0
    elif amount == 0:
        return 1
    else:
        return counter(amount-lst[-1], lst) + counter(amount, lst[:-1])

def counter2(amount, lst):
    if not lst:
        return 0
    elif amount <= 0:
        return 1
    elif amount >= lst[-1]:
        return counter(amount-lst[-1], lst) + counter(amount, lst[:-1])
    else:
        return counter(amount, lst[:-1])    
    

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k)) (lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
