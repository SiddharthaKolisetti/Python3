def prime(n):
    prime_array=[]
    for num in range(2,n):
        for i in range(2,num):
            if (num%i)==0:
                    break
        else:
            prime_array.append(num)
    return prime_array
print(prime(23))
