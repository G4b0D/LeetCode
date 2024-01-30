def LenghtOfLastWord(s:str) -> int:
    count = 0
    lcount = 0
    for c in s:
        count += 1
        if c == " ":
            count = 0
        elif c.isalpha():
            lcount = count
    return lcount

def LenghtOfLastWord2(s:str) -> int:
    i = len(s) - 1
    lenght = 0

    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        lenght += 1
        i -= 1
    return lenght

print(LenghtOfLastWord2("Luffy is JoyBoy"))

        