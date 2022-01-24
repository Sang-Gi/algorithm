input = 20


def find_prime_list_under_number(number): # 에라토스테네스의 체
    # 변수에 범위 set
    num = set(range(2, number + 1))

    # 반복문
    for i in range(2, number + 1):
        if i in num:
            num -= set(range(2 * i, number + 1, i)) 
            # 소수는 배수가 아닌 수
            # 따라서 배수인 수를 배열에서 제외해줌
    return num


result = find_prime_list_under_number(input)
print(result)