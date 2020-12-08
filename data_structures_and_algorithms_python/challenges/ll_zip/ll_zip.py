class linkedlist():    
    
    def zip(ll1,ll2):
        head = node(0)
        pointer = head
        while true:
            if ll1 is none and ll2 is none:
                return "empty"
            elif ll1 is none:
                pointer.next = ll2
                break
            elif ll2 is none:
                pointer.next = ll1
                break
            else:
                value = 0
                if ll1.value < ll2.value:
                    value = ll1.value
                    l1 = l1.next
        
                    


