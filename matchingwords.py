a="Hello everyone , have a pleasant day"
b="Good Morning everyone , such a pleasant weather"
def match(a,b):
    m=a.split()
    n=b.split()
    c=[]
    for i in m:
        if i in n:
            c.append(i)
    return c
print(match(a,b)) 