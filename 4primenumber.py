def num(x):
    for i in range(2,int(x/2)+2):
        if x%i==0 :
            return False
            break
        #print(i)
        if i==int(x/2)+1:
            return True

print(num(93))
print(num(32))
