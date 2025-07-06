n=30
a1,a2=1,2
fib=[1,2]
for i in range(n):
    a1,a2=a2,a2+a1
    fib.append(a2)
fib_even=[x for x in fib if x%2==0]

print(sum(fib_even))
