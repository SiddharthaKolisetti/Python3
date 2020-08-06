c=int(input("Enter a number:"))
b=0
temp=0
if c>0:
    while c!=0:
        b=c%10
        temp=(10*temp)+b
        c=c//10
    print(temp) 
if c<0:
    c=-c
    while c!=0:
        b=c%10
        temp=(10*temp)+b
        c=c//10
    print(-temp) 