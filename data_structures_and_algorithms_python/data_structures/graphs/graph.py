from queue import Queue 

class Node:
    def __init__(self, value):
        self.value = value


class Graph():
    def __init__(self):
        self.list = {}

    def add_node(self, value):
        self.value = Node(value)
        self.list[node] = []


    def breadth_first(self, start):
        nodes = []
        visited_nodes = set()
        br = Queue()
        br.enqueue(start)
        visited.add(start)

        while len(br)


