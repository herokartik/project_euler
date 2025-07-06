from collections import Counter
N=[]
for x in range(1,1000000):
    a=2*x
    b=3*x
    c=4*x
    d=5*x
    e=6*x
    list_x=[int(g) for g in str(x)]
    list_a=[int(g) for g in str(a)]
    list_b=[int(g) for g in str(b)]
    list_c=[int(g) for g in str(c)]
    list_d=[int(g) for g in str(d)]
    list_e=[int(g) for g in str(e)]
    if Counter(list_x)==Counter(list_a)==Counter(list_b)==Counter(list_c)==Counter(list_d)==Counter(list_e):
        N.append(x)
print(N)
