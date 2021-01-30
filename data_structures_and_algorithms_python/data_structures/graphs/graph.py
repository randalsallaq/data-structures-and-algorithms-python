

class Node:
    def __init__(self, value):
        self.value = value


class Graph():
    def __init__(self):
        self.mylist = {}

    def add_node(self, value):
        self.value = Node(value)
        self.mylist[node] = []


    def breadth_first(self, start):
        nodes = []
        visited_nodes = set()
        br = Queue()
        br.enqueue(start)
        visited.add(start)

        while len(br)> 0:
            node = br.queue
            nodes.append(node)
            for i in list[node]:
                if i not in visited_nodes:
                    br.enqueue(n)
                    visited_nodes.add(i)
        return nodes

    def add_edge(self, start, end, weight=1):
        self.mylist[start][end] = weight
        self.mylist[end][start] = weight 

        

    def get_nodes(self):
        array = []
        for i in self.list:
            array.append(i)
        return array

    def get_neighbours(self):
        return self.mylist[node]



    def size(self):
        return len(self.mylist.keys)


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(3)
    graph.add_node(5)
    graph.add_node(7)
    graph.add_node(9)
    graph.add_edge(5,7,9)
    print(graph.mylist)

    graph.add_edge(10,30,9)
    graph.add_edge(5,10,9)
    graph.add_edge(5,20,1)
    graph.add_edge(5,30,3)
    print(graph.mylist)
    print(graph.bfs(10))
    print(graph.get_nodes())
