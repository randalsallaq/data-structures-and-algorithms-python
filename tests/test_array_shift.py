from data_structures_and_algorithms_python.challenges.array_shift.array_shift import insert_shift_array

def test_shifting():
    a = [1,2,3,5,6,7]
    actual = insert_shift_array(a,4)
    expected = [1,2,3,4,5,6,7]
    assert actual == expected 