def reverse_array(arr):
    """Reverses a list
    Args:
        arr (list): python list
    Returns:
        [list]: list in reversed form
    """
    # put your function implementation here

    update_list = []
    list_length = len(arr)
    while list_length:
        update_list.append(arr[list_length-1])
        list_length-=1
    return arr

