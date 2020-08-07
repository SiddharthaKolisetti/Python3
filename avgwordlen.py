a=input("Enter a sentence:")
b=0
l=[]
j="!@#$%^&*,.:/?"
for i in a:
    if i in j:
        a=a.replace(i, '')
l=a.split()
c=len(l)
for i in l:
    b+=len(i)
d=round((b/c), 2)
print(b)
print(c)
print(d)