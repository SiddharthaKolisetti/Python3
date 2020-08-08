a={}
def unique(str):
    for i in str:
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    for i in range(len(str)):
        if a[str[i]]==1:
            return i
    return -1
print(unique('hello'))
print(unique('siddhu'))