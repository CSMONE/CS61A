def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    max_num = max(a, b)
    min_num = min(a, b)

    if min_num == 1:
        return 1
    elif max_num % min_num == 0:
        return  min_num
    else:
        return gcd(min_num, max_num % min_num)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
     If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 
     Repeat this process until n is 1

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0:
        print(n)
        return hailstone(n // 2) + 1
    else:
        print(n)
        return hailstone(n * 3 + 1) + 1

