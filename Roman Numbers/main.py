def RomanToInt2(s:str):
    ROMAN_NUMS = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    reversed_str = s[::-1]
    res = 0
    prev_value = 0
    for c in reversed_str:
        value = ROMAN_NUMS[c]
        if value < prev_value:
            res -= value
        else:
            res += value
        prev_value = value
    return res
def RomanToInt(s:str):
    ROMAN_NUMS = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    nums = []
    for i,c in enumerate(s):
        value = ROMAN_NUMS[c]
        if i+1 < len(s):
            if value < ROMAN_NUMS[s[i+1]]:
                value *= -1
        nums.append(value)
    return sum(nums)

print(RomanToInt2("MCMXCIV")) 