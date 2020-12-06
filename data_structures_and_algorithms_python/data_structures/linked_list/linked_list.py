class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None



    def __repr__(self):
        return "create linked list"


    def insert(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current_value = self.head
        while current_value:
            if current_value.value == value:
                return True
            else:
                current_value = current_value.next
            return False

    def __str__(self):
        list_str = ''       #another way[]
        current = self.head
        while current:
            
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]

    def append(self, value):
        current = self.head
        while current:


            print(current.value)
            if current.next == None:
                current.next = Node(value)
                return self.__str__()
            else:
                current = current.next

        self.head = Node(value)
        return self.__str__()

    def insert_before(self, value, new_value):
        if self.includes(value):
            current = self.head
            previous = None
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    return self.__str__()
                previous = current
                current = current.next
        else:
            return 'Value is not in the list'


    def insert_after(self, value, new_value):
        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next
        else:
            return 'There is no value'

    def length(self):
        length = 0
        current = self.head
        while current:
            length+=1
            current = current.next
        return length

    def from_end(self, value):
        length = self.length()

        count = None

        if value >= 0:
            count = length - value -1
        if value < 0:
            count = abs(value)-1

        current = self.head
        for _ in range(count):
            current = current.next
        return current.value

