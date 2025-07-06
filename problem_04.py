num=[]
for i in range(101,1000):
    for j in range(101,1000):
        k=i*j
        k_str=str(k)
        k_str_rev=k_str[::-1]
        if k_str==k_str_rev:
            num.append(int(k_str))
print(max(num))

