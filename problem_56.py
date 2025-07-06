N=[]
for i in range(1,101):
    for j in range(1,101):
        k=i**j
        N.append(k)
SUM=[]
for m in range(0,len(N)-1):
    num_list=[int(d) for d in str(N[m])]
    num_sum=sum(num_list)
    SUM.append(num_sum)
print(max(SUM))

