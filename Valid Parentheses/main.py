def IsValid(s):
    OPPENERS = ['[','{','(']
    CLOSERS = [']','}',')']
    found_symbols = []
    if len(s) <= 1:
        return False
    for c in s:
        if c in OPPENERS:
            found_symbols.append(c)
            continue
        if len(found_symbols) == 0 or not OPPENERS[CLOSERS.index(c)] in found_symbols[-1]:
            return False
        found_symbols.pop()
    return len(found_symbols) == 0 if found_symbols else True

print(IsValid("{()}"))


