def prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    else:
            return True
N=[]
for p in range(2,300000):
    if prime(p) is True:
        N.append(p)
print(N[10000])

