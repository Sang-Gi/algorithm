input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrenece = alphabet_occurrence_array[index]
        if alphabet_occurrenece == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string: # 이 반복문을 통해 바로 조건 완성되면 출력 
        if char in not_repeating_character_array:
            return char
        
    return "_"

result = find_not_repeating_first_character(input)
print(result)