a=int(input('enter the number of students for enterin details:- '))
dic={}
for i in range(a):
    b=int(input('enter roll no. :- '))
    c=input('enter name :- ')
    d=int(input('enter age :- '))
    dic[b]=['name : ',c,'age : ',d,' years']
print (dic)