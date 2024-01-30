def strStr(haystack:str, needle:str) -> int :
    if needle in haystack:
        return haystack.index(needle)
    return -1

#Using KPM algorithm https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def strStr2(haystack: str, needle:str) -> int:
        """
        needle: AAAKA
        LPS: [0,1,2,0,1]
        """
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1

s = "BAAAAAAKA"
search = "AAAKA"
print(strStr2(s,search))
