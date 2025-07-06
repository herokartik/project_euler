import math
x=math.factorial(100)
x_s=str(x)
lst=list(x_s)
digit_sum=sum(int(d) for d in lst)
print(digit_sum)
