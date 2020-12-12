def zip(one,two):
    if one.length() == 0 and two.length() ==0:
        return 'empty'

    if one.length()==0:
        return two.__str__()
    
    if two.length()==0:
        return one.__str__()  

    pointer_one=one.head
    first_step=pointer_one.next

    pointer_two=two.head
    second_step=pointer_two.next
 

    while pointer_one:
        if pointer_two:
            pointer_one.next=pointer_two
            pointer_one=first_step
            if first_step:
                first_step=first_step.next
            if pointer_one:
                pointer_two.next=pointer_one
                pointer_two=second_step
                if second_step:
                    second_step=second_step.next
        else:
            break            

    return one.__str__()