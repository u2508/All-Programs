#question 1. 
a= input('enter string :- ')
new=''
for b in a:
    if b.isnumeric()==True:
       new=new +'0'
    elif b=='z':
        new+='a'
    elif b=='Z':
        new+='A'
    elif b.isalpha()==True:
        new+=chr(ord(b)+1)
print ('the new string is',new)
#question 2.
a= input('enter some words :- ')
new=''
a=a.split( )
for i in range(0,len(a)):
    new+=a[i]
print(a,new)
