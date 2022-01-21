input = "abcba"


def is_palindrome(string):
    
    n = len(string)

    for i in range(n):
        if string[i] != string[n - 1 - i]: # i번째와 n - 1 - i(맨 뒤에서 i 만큼 앞)가 다르면 False
            return False
    return True # 외에 같으면 True


print(is_palindrome(input))