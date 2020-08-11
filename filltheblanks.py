a=[1,2,None,3,None,None,4,None]
def fill(l):
    b=[]
    for i in l:
        if i!=None:
            b.append(i)
        elif i==None:
            i=b[-1]
            b.append(i)
    return b
print(fill(a))
            