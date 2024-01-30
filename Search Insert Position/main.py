def SearchItem(nums:list[int],val: int) -> int :
    """
    Solution in O(logn) using binary search
    Binary Search: Algorithm that slices a sorted array in half every time to search for an element. A middle pointer is determined, if the target value is bigger than the middle pointer the left pointer is moved to the middle +1, else the right pointer is moved to the middle -1. If the left pointer value is greater than the right pointer value we can assume the value was not found. For this problem it is required to return the possible index for the target value, so the function returns the left pointer.
    """
    l =0 #left pointer
    r = len(nums)-1 #right pointer

    while l<=r:
        m = (r+l)//2
        if nums[m] == val:
            return m
        elif nums[m] > val:
            r = m -1
        else:
            l = m +1
    return l

nums = [1,2,3,5,6,7,22]
print(SearchItem(nums,23))