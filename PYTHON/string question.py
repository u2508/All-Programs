def question1():
    #program to capitalize alternate letters
    n=input('enter a string:- ')
    new=''
    if n.isalpha()==True:
        for a in range(0,len(n)):
            if a%2==0:
                new+=(n[a].capitalize())
            else:
                new+=n[a]
        print(new)
    else:
        n=input('enter a string properly:- ')
def question2():
    #program to convert a str into '*********' form
    p=input('enter a random password :- ')
    new=''
    new+=('*'* len(p))
    print(new)
a=int(input('For which question do you need the answer and if you want to exit enter 0 :- '))
if a==1:
    question1()
elif a==2:
    question2()
elif a==0:
    print('exiting'.capitalize(),'the program with code (0).')
    SystemExit
else:
    a=input('1,2 are the  only valid responses for question ,so enter again or enter 0 to exit :- ')