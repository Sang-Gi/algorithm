input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    a = len(array)

    for i in range(a - 1):
        for j in range(a - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return

bubble_sort(input)
print(input)  # 시간 복잡도 : O(N^2)