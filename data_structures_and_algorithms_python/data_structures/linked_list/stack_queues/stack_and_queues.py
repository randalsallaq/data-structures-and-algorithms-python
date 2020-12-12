class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def push(self, value):
        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top
            self.top = self.top.next
            popped.next = None
            return popped.value
        else:
            return None