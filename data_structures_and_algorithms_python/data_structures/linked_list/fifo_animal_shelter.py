# instead of importing
class Node:
    def __init__(self, value):
        self.value = value
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
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


 def enqueue(self, node):
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

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


class Animal:
    def __init__(self, name):
        self.value = name
        self.next = None

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'dog'


class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.queue1.enqueue(animal)
        else:
            return "Animal must be cat or dog"

    def dequeue(self, pref):
        animal_new = None
        while not self.queue1.is_empty():
            if self.queue1.front.type == pref.lower() and animal_new == None:
                animal_new= self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return animal_new
