#!/usr/bin/env python

def reverse(n):
    """
    This function reverses the digits of a given integer.

    >>> reverse(234)
    432
    """
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n // 10
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
