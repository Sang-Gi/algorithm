class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # head
    # [3] -> [4]

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty !"
        delete_head = self.head
        self.head = self.head.next
        
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty !"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3) # 3
print(stack.peek()) # 3

stack.push(4) # 4 3
stack.push(5) # 5 4 3
print(stack.peek()) # 5

stack.pop() # 4 3
print(stack.peek()) # 4

print(stack.is_empty()) # False
stack.pop() # 3
stack.pop() # empty
print(stack.is_empty()) # True
