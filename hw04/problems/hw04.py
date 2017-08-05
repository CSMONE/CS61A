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
    g_list = []
    for i in range(n):
        if i < 3:
            g_list.append(i + 1)
        else:
            g_list.append(g_list[i - 1] + 2 * g_list[i - 2] + 3 * g_list[i - 3])
    return g_list[n - 1]

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
    def rec_func(i, k, up):
        if i == n:
            return k
        if has_seven(i) or i % 7 == 0:
            return rec_func(i + 1, k - up, - up)
        else:
            return rec_func(i + 1, k + up, up)

    return rec_func(1, 1, 1)

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
    def rec_func(n, k):
        if n == 0 or k == 0:
            return 1
        elif n < 0 or k < 0:
            return 0
        else:
            return rec_func(n - 2**k, k) + rec_func(n, k - 1)

    i, m = 0, 1
    while m * 2 < amount:
        i, m = i + 1, m * 2

    return rec_func(amount, i)




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

    
    def rec_func(n):
        if n == 1:
            return 1
        else:
            return n * rec_func(n-1)
    return rec_func
    """

    return lambda n: (lambda f, v: f(f, v))(lambda f, v: 1 if v == 1 else mul(v, f(f, sub(v, 1))), n)
