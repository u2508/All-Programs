n=input("enter a num :- ")
n1=int(n[::-1])
sum=0
for (i) in str(n1):
    sum+=int(i)
    print(sum)
print('reversed num is',n1)