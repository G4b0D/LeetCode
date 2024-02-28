"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
"""
def MergeSortedArray(a:list[int],b:list[int],m:int,n:int):
    """
    a: First list of numbers with len m+n.
    b: Second list of numbers with len n.
    m: The amount of elements from the beggining of a that should be merged.
    n: The amout of elements from the end of b that should be merged.
    """
    last = m+n-1

    while m>0 and n>0:
        if a[m-1] > b[n-1]:
            a[last] = a[m-1]
            m -= 1
        else:
            a[last] = b[n-1]
            n -=1
        last -= 1
    while n>0:
        a[last] = b[n-1]
        n,last = n-1, last-1
    return a

a= [1,1,2,3,4]
b = [5,7,9]

a = MergeSortedArray(a,b,3,2)
print(a)