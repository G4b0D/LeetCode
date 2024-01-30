def AddBinary(a:str,b:str) -> str:
    maxLen = max(len(a),len(b))
    a = a.zfill(maxLen)
    b = b.zfill(maxLen)

    result = []
    carry = 0

    for i in range(maxLen-1,-1,-1):
        bit_sum = (int(a[i]) + int(b[i])) + carry
        result.insert(0,str(bit_sum%2))
        carry = bit_sum // 2

    if carry:
        result.insert(0,str(carry))
    return ''.join(result)
    
bin1 = '11'
bin2 = '11'
print(AddBinary(bin1,bin2))
