import time
L=[2,3,4,2,1,5,4]
x=L[len(L)-1]
for i in range(len(L)-1,-1,-1):
    if i==0:
        L[i]=x
    else:
        L[i]=L[i-1]
print(L)
time.sleep(2)
print(' ')
n=65
l=[]
for j in range(1,27):
    c=chr(n)
    d=c*j
    l.append(d)
    n+=1
print(l)