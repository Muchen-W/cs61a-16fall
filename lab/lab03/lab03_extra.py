from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + 10 * y
    while x > 0:
        x, y = x // 10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i <= n:
            print(i)
            counter(i+1)
    counter(1)


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a < b:
        a, b = b, a
    if b == 0:
        return c
    else:
        return ab_plus_c(a, b-1, c) + a
        

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n == 2:
        return True
    def division(i):
        if i == n:
            return True
        if n % i == 0:
            return False
        else:
            return division(i + 1)
    return division(2)


def interleaved_helper(n, odd_term, even_term):
    if n == 1:
        return odd_term(1), even_term, odd_term
    else:
        total, term0, term1 = interleaved_helper(n-1, odd_term, even_term)
        return total + term0(n), term1, term0

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    # solution 1 with interleaved_helper function
    return interleaved_helper(n, odd_term, even_term)[0]

    # solution 2 with two interleaved def functions
    def odd_sum(i, total):
        total += odd_term(i)
        if i == n:
            return total
        else:
            return even_sum(i+1, total)

    def even_sum(i, total):
        total += even_term(i)
        if i == n:
            return total
        else:
            return odd_sum(i+1, total)

    return odd_sum(1, 0)


def counter(k, n):
    if n == 0:
        return 0
    elif n % 10 == k:
        return counter(k, n//10) + 1
    else:
        return counter(k, n//10)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    return sum([counter(i, n) * counter(10-i, n) for i in range(1, 5)]) + counter(5, n) * (counter(5, n) - 1) // 2
