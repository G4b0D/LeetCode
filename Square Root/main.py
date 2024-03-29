#https://leetcode.com/problems/sqrtx/description/
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""
def sqrt(n: int) -> int:
    """
    Get square root of int without using built in functions. Returns rounded down value for decimal results. Eg: sqrt(5) --> 2
    """
    if n == 0 or n == 1:
        return n
    res = 0
    l,r = 0, n
    # Binary Search Time!
    while l <= r:
        m = (l+r) // 2
        square = m * m

        if square == n:
            return m
        elif square < n:
            l = m +1
            res = m
        else:
            r = m - 1
    return res


print(sqrt(8))