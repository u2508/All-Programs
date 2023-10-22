# program to illustrate all the following 
# codes one by for given patterns
#question1 output
'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
'''
for num in range (1,7):
    cas=65
    for a in range (0,num):
        b=chr(cas)
        print(b,end=' ')
        cas+=1
    print('')
import time
time.sleep(2)
print(" ")
#question2 output
'''
A
BB
CCC
DDDD
EEEEE
'''
n=65
for j in range(1,6):
    for i in range(0,j):
        c=chr(n)
        print(c,end='')
    print('')
    n+=1
time.sleep(2)
print(' ')
#question3 output
'''
********
 ******
  ***
   *
'''
n=8
space=n//2*2
for row in range(0,n+1,2):
    for a in range(0,row+1):
        print(end=' ')
    for sp in range(0,space+1):
        print(end=' *')
    print()
    space-=2
time.sleep(2)
print(' ')
#question4 output
'''
0
1
1
2
3
5
8
13
21
34
'''
n1=0
n2=1
print(n1,n2,sep='\n',end="\n")
for i in range (1,9):
    n3=n1+n2
    print(n3,end='\n')
    n1,n2=n2,n3
time.sleep(2)
print(' ')
#question5
#program to find lcm and hcf of two numbers
x=int(input('ENTER FIRST NUMBER :- '))
y=int(input('ENTER SECOND NUMBER :- '))
MIN=min((x,y))
Cf=[]
for i in range(1,MIN+1):
    if ((x%i==0)and(y%i==0)):
       Cf.append(i)
else:
    hcf=max(Cf)
    lcm=int((x*y)/hcf)
    print('h.c.f of',x,'and',y,'is',hcf)
    print('l.c.m of',x,'and',y,'is',lcm)