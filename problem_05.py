import sys
sys.set_int_max_str_digits(500000)

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b)//gcd(a,b)
result=1
for i in range(1,21):
    result=lcm(result,i)
print(result)
