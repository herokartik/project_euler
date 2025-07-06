from num2words import num2words
arr=[]
for i in range(1,1001):
    x=num2words(i)
    x_cln=x.replace(" ","").replace("-","")
    lst=list(x_cln)
    arr.extend(lst)
print(len(arr))
