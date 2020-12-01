from data_structures_and_algorithms_python.challenges.array_binary_search.array_binary_search import binary_search


def test_binary():
    a= [1,2,3,8,20]
    b = 8
    actual = binary_search(a,b)
    expected = 2
    assert actual == expected
    


def test_binary_not():
    a = [5,10,15,20,25]
    b = 30
    actual = binary_search(a,b)
    expected = -1
    assert actual == expected   