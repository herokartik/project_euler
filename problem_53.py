from math import factorial
arr=[]
for n in range(1,101):
    for r in range(1,101):
        if n-r>0:
            den=factorial(n)
            num=factorial(r)*factorial(n-r)
            npr=den/num
            if npr>1000000:
                arr.append(npr)
print(len(arr))

