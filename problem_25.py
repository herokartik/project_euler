n=4781
a1,a2=1,2
fib=[1,2]
for i in range(n):
    a1,a2=a2,a2+a1
    fib.append(a2)
print(len(str(fib[n-1])))
