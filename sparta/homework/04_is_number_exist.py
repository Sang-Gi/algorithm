input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array: # array의 길이 만큼 아래 연산 실행
        if number == element: # 비교연산 실행
            return True
                   # N * 1 = N 만큼의 시간 복잡도
    return False


result = is_number_exist(9, input)
print(result)