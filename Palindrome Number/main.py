def isPalindrome(num:int):
    if num < 0:
        return False
    if num == 0:
        return True
    num_string = str(num)
    return num_string[::-1] == num_string


def isPalindrome2(x:int):
    if x < 0:
        return False

    original_x = x
    reversed_x = 0

    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    return original_x == reversed_x


print(isPalindrome2(456))