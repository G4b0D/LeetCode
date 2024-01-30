def PlusOne(nums: list[int]) -> list[int]:
    num = 0
    for i,n in enumerate(nums):
        num = (num+n)
        if i < len(nums)-1:
            num *= 10
    return [int(i) for i in str(num+1)]


print(PlusOne([9]))