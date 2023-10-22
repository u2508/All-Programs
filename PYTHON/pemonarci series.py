n1=0
n2=1
l=[]
for i in range (1,11):
    if i==1:
        l.append(n1)
    elif i==2:
        l.append(n2)  
    else:
        n3=n1+n2
        l.append(n3)
        n1,n2=n2,n3
print(l)