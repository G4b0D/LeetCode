nums = [-1,0,0,0,0,3,3]
def RemoveDuplicates(nums:list[int]) -> int:
    unique_nums = {i:None for i in nums}
    for i,n in enumerate(list(unique_nums.keys())):
        nums[i] = n
        print(n)
    #print(nums)
    return len(list(unique_nums.keys()))
print(RemoveDuplicates(nums))
print(nums[:RemoveDuplicates(nums)])