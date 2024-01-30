#https://leetcode.com/problems/sqrtx/description/
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