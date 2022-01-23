input = "abccba"
# 회문검사 재귀함수로 구현.

def is_palindrome(string):
    if len(string) <= 1: # "소주만병만주소" | 가운데 "병"만 남았을때 조건문
        return True

    if string[0] != string[-1]:
        return False
    
    return is_palindrome(string[1:-1])


print(is_palindrome(input))