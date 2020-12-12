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
    test_stack.pop()
    test_stack.pop()
    
