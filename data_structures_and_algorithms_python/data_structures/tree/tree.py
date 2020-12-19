class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.next = None
        
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        new_node = node

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
            return temp
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.front.value
        return None