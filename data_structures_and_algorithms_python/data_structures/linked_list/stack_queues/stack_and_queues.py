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
            ##

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            return None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False


    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            return None
       