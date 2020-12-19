from data_structures_and_algorithms_python.data_structures.linked_list.stack_queues.stack_and_queues import *


def create_stack(nodes):
    test_stack = Stack()
    for el in nodes:
        test_stack.push(el)
    return test_stack


def test_Node_created():
    node_a = Node('a')
    assert 'a' == node_a.value
    assert None == node_a.next

def test_stack_empty():
    test_stack = Stack()
    assert test_stack.top == None

def test_stack_push():

    test_stack = Stack()
    assert test_stack.top == None
    test_stack.push(5)
    assert test_stack.top.value == 5
    test_stack.push('b')
    assert test_stack.top.value == 'b'
    test_stack.push('c')
    assert test_stack.top.value == 'c'

def test_stack_pop():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.pop() == 'd'
    assert test_stack.top.value == 'c'
    assert test_stack.top.next.value == 'b'
    test_stack.pop()
   
def test_stack_peek():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.peek() == 'd'
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.peek() == None
##########################################################\

def test_stack_is_empty():
    test_stack = create_stack(['a', 'b', 'c', 'd'])
    assert test_stack.is_empty() == False
    test_stack = Stack()
    assert test_stack.is_empty() == True


def create_queue(nodes):
    """create a queue"""
    test_queue = Queue()
    for el in nodes:
        test_queue.enqueue(el)
    return test_queue


def test_queue_empty():
    test_queue = Queue()
    assert test_queue.front == None
    assert test_queue.rear == None

def test_queue_enqueu():
    test_queue = Queue()
    assert test_queue.front == None
    test_queue.enqueue(5)
    assert test_queue.front.value == 5
    test_queue.enqueue('b')
    assert test_queue.rear.value == 'b'

def test_queue_dequeue():
    test_queue = create_queue(['a', 'b', 'c', 'd'])
    assert test_queue.dequeue() == 'a'
    test_queue.dequeue()
 
 


    

