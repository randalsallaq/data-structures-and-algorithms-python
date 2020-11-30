def insert_shift_array(array, value):
    length = len(array)
    index = length //2
    array2 = []
    index2 = 0
    for i in range(length + 1):
        if i == index:
            array2.append(value)
        else:
            array2.append(array[index2])
            index2 += 1  

    return array2       
    