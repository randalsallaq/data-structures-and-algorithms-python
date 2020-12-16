l1=['{','(','[']
l2=['}',')',']']
def multibracketvalidation(input):
    stack=[] 

    for i in input:
        if i in l1:
            stack.append(i) 
        elif i in l2:
            index = l2.index(i)
            if len(stack) > 0 and l1 [index] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
            
    if len(stack) == 0:
        return True
    else:
        return False

print(multibracketvalidation('()[[Extra Characters]]'))
print(multibracketvalidation('{[]{(])}}'))