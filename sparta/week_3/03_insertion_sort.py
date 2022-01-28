input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i): # i가 늘어날떄마다 내부 반복문 j도 증가
            if array[ i - j - 1 ] > array[ i - j ]:
                array[ i - j - 1 ], array [ i - j ] = array[ i - j ], array[ i - j - 1 ]
            else:
                break # 교체 후 숫자 변경 필요없으면 반복문 종료.

insertion_sort(input)
print(input) # 시간 복잡도 : O(N^2)