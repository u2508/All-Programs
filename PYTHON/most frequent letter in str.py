#program to find the most frequent letter in str
a=tuple(input('enter the string:- '.capitalize()))
b={}
c=[]
for i in a:
    b.update({i:a.count(i)})
    c=b.values()
    d=[number for number,name in b.items() if name==max(c)]
print('The most frequently used letter in this string are',end=' ')
for j in range(0,len(d)-1):
    print(d[j],end=',')
print(d[len(d)-1],'occuring',max(c),'times each.')