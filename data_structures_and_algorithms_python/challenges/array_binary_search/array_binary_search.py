def binary_search(array,key):
    test_length = 0
    while True:
        try:
            array[test_length]
        except IndexError:
            break
        else:
            test_length += 1
            continue
    array_length = test_length

    array_index = array_length-1

    mid = array_length // 2

    while array[mid] != key:
        if key > array[array_index]:
          return -1
          
        if key == array[mid]:
            return mid
        if key < array[mid]:
            mid = mid // 2
        if key > array[mid]:
            mid = array_index-mid  

    return mid  

    