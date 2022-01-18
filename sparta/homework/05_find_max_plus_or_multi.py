input = [6, 3, 5, 0, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for num in array:
        if num <= 1 or answer <= 1:
            answer += num
        else:
            answer *= num
    return answer

result = find_max_plus_or_multiply(input)
print(result)