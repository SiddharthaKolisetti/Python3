def num(x):
    for i in range(2,x+1):
        if x%i==0 and i!=x:
            return False
            break
        #print(i)
        if i==x:
            return True

print(num(2))