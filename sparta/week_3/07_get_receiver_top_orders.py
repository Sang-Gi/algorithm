top_heights = [6, 9, 5, 7, 4]

#   <- <- <- <-
#  6  9  5  7  4

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    while heights: # heights가 빈상태가 아닐때까지 반복.
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1): # 5까지 반복, 0부터, 역순으로
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    
    return answer

print(get_receiver_top_orders(top_heights))  # 시간 복잡도 : O(N^2)