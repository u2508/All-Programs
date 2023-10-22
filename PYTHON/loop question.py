#question1
def question1 () :
    n= int(input('enter a year :- '))
    if n%4==0:
        if n%100==0 and n%400!=0:
            print('it'.capitalize(),'is not a leap year.')
        else:
            print('it'.capitalize(),'is a leap year.')
    else:
        print('it'.capitalize(),'is not a leap year.')
#question2
def question2 ():
    n= int(input('enter number of odd numbers to be printed in  decending order :- '))
    a=1+(2*(n-1))
    for i in range(a,0,-2):
        print(i,end=' ')
#question3
def question3 ():
    for i in range(1,41,3):
        print(i,end=' ')
def question4 ():
    n= int(input('enter a number greater than 20 :- '))
    if n<=20:
        n= int(input('enter a number greater than 20 :- '))
    for i in range(11,n+1):
        if i%3==0 and i%7==0:
            print(i,end=' Tipsy Topsy ')
        elif i%3==0:
            print(i,end=' Tipsy ')
        elif i%7==0:
            print(i,end=' Topsy ')
        else:
            print(i,end=' ')
a=int(input('For which question do you need the answer and if you want to exit enter 0 :- '))
if a==1:
    question1()
elif a==2:
    question2()
elif a==3:
    question3()
elif a==4:
    question4()
elif a==0:
    print('exiting'.capitalize(),'the program with code (0).')
    SystemExit
else:
    a=input('1,2,3,4 are the  only valid responses for question ,so enter again or enter 0 to exit :- ')