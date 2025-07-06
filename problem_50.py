num=[]
def prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    else:
            return True
for i in range(1,3900):
    if prime(i)==True:
        num.append(i)
n_prime=sum(num)
lst=[]
while prime(n_prime)==True:
    lst.append(num)
print(lst)
