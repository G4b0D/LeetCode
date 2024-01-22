def GetCommonPrefix(strings:list[str]) -> str:
    common_letters = [c for c in strings[0]]
    for s in strings[1:]:
        if len(common_letters) == 0 or len(s) == 0:
            return ""
        for i,c in enumerate(common_letters):
            if i >= len(s):
                if i >= 1:
                   common_letters = common_letters[:i] 
                break
            if c != s[i]:
                common_letters = common_letters[:i]
                break
    return ''.join(common_letters)
            
print(GetCommonPrefix(["ab","a"]))


            
                
    