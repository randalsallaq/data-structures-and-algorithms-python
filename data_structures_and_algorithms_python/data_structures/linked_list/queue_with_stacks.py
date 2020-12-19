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
        node = Node(value)
        node.next = self.top 
        self.top = node



        def pop(self):
        if not self.is_empty():
            temp = self.top 
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
         if not self.is_empty():
            return self.top.value
        else:
            return None

    
    class PseudoQueue:
    def __init__(self, stack):
        self.stack = stack
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        if self.stack.top == None:
            raise Exception("there is no values")
        while self.stack.top != None:
            popped = self.stack.pop()
            self.stack2.push(popped)
        pop_val = self.stack2.pop()

        while self.stack2.top != None:
            self.stack.push(self.stack2.pop())
        return pop_val