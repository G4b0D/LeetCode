def removeElement(nums: list[int], val: int) -> int:
    nums2 = [i for i in nums if i != val]
    for i,n in enumerate(nums2):
        nums[i] = n
    return len(nums2)
nums = [0,1,2,2,3,0,4,2]
removeValue = 2
print(f"Original List: {nums}")
print(f"Assorted values count: {removeElement(nums,removeValue)}")
print(f"Assorted List: {nums}")