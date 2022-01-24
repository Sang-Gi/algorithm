class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        count = 1 # 노드의 길이를 알아내기위한 카운터
        cur = self.head # cur는 현재, 시작점부터 시작

        while cur.next is not None: # 노드끝까지 돌려서 노드의 길이를 count에 저장
            cur = cur.next
            count += 1
        
        node_len = count - k # 노드의 길이에서 k만큼 뺀 수
        
        cur = self.head # cur 재지정
        for i in range(node_len):
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!