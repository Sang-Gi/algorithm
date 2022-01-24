input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    countZero = 0
    countOne = 0

    # index 0의 원소 파악
    if string[0] == '0':
        countOne += 1 # 0일땐, 1로 바꿔주어야하니 count + 1
    elif string[0] == '1':
        countZero += 1 # 1일땐, 0으로 바꿔주어야하니 count + 1
    
    # 반복문을 통해 string 훑기
    for i in range(len(string)):
        if string[i-1] != string[i]:
            if string[i] == '1':
                countZero += 1
            elif string[i] == '0':
                countOne += 1
    return min(countOne, countZero)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# https://www.notion.so/1-9c4497df09324035a3f3e212f7a43f94#6d13d13eaf12469ba069f52bcfbb33ff