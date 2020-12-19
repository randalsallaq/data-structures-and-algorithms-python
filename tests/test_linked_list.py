
from data_structures_and_algorithms_python.data_structures.linked_list.linked_list import *

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_Node_created():
    assert 3 == Node(3).value
    assert None == Node(3).next

def test_insert_to_empty():
    val = 5
    linked_list = LinkedList()
    linked_list.insert(val)
    assert linked_list.head.value == 5

def test_head_first():
   linked_list = LinkedList()
   linked_list.insert('a')
   assert linked_list.head.value == 'a'



linked_list = LinkedList()
new_nodes = ['a', 'b', 5, 'dfa', ['t', 'r', 4]]
for node in new_nodes:
    linked_list.insert(node)

def test_include():
    assert linked_list.includes('dfa') == True

def test_notinclude():
    assert linked_list.includes('daf') == False


def test__str__():
    assert linked_list.__str__() == "['t', 'r', 4], dfa, 5, b, a"


    ###

def test_append():
    assert "d, 4, b, a, z" == linked_list.append('z')



def test_insert_after_value_in_list():
    assert "d, 4, b, 3, cat, a, z" == linked_list.insert_after('cat', 'a')


def test_ll_insert_before(ll, filled_ll):
   
    ll.insert_before(2, 6)
    assert ll.head == None

    ll.append(2)
    assert ll.head.value == 2
    
    ll.insert_before(23, 5)
    assert ll.head.value == 3
    assert '3, 1, 2, 5, 8' == ll.insert_before(8, 5)
    assert ll.head.next.next.next.value == 5
    assert ll.head.next.next.next.next.value == 8

