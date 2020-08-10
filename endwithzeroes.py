a=[1,2,0,3,0,0,0,5,6]
b=[100,2,3,0,7,0,5,4,3]
def end(s):
    for i in s:
        if 0 in s:
            s.remove(0)
            s.append(0)
    return s
print(end(a))
print(end(b))
