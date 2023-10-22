# program to segregate uniques and duplicates
l1=(list(eval(input('enter a list:'))))
lre=[]
luni=[]
for i in range(0,len(l1)):
         if l1[i] in l1[i+1:]:
                  if l1[i] not in lre:
                           lre.append(l1[i])
         else:
                  if l1[i] not in lre:
                           luni.append(l1[i])
print('list is',l1)
print('repeated numbers are',lre)
print('unique numbers are',luni)
#                       Or
'''program to segregate uniques and duplicates in some different ways
l1=(list(eval(input('enter a list:'))))
l2=[]
l3=[]
for a in l1 :
    b=l1.count(a)
    if b==1 :
        l2.append(a)
    else:
        l3.append(a)
        lenght=len(l3)-1
        if l3.count(a)>1:
            l3.remove(l3[lenght])
print('uniques are',l2,'and duplicates are',l3)'''