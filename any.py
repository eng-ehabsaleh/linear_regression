def check(s):
    if len(s)%2!=0:
       return False
    opening = set('[{(')
    matching = set([('[',']'),('{','}'),('(',')')])
    stack =[]
    for p in s:
        if p in opening:
            stack.append(p)
        else:
            if len(stack)==0:
                return False
            if p in opening:
             L = stack.pop()
             if (L,p) not in matching :
                return False
    return True
    
    
print(check("{(}")) 