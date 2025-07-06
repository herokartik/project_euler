def prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    else:
            return True
N=[]
for i in range(2,2000000):
    if prime(i)==True:
        N.append(i)
print(sum(N))

