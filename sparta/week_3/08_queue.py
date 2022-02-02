class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty !"
        
        delete_head = self.head
        self.head = self.head.next
        
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty !"
        
        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3) # 3
print(queue.peek()) # 3
queue.enqueue(4) # 3 4
print(queue.peek()) # 3
queue.enqueue(5) # 3 4 5
print(queue.peek()) # 3
queue.dequeue() # 4 5
print(queue.peek()) # 4
queue.dequeue() # 5
print(queue.peek()) # 5
queue.dequeue() # empty
print(queue.peek()) # Queue is empty !
