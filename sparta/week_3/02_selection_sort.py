input = [4, 6, 2, 9, 1]


def selection_sort(array):
    a = len(array)

    for i in range(a - 1):
        min_index = i # array에서 최소값을 찾는 변수
        for j in range(a - i):
            if array[i + j] < array[min_index]:
                min_index = i + j
            array[i], array[min_index] = array[min_index], array[i]

selection_sort(input)
print(input) # 시간 복잡도 : O(N^2)