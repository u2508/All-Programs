import time,math
a=int(input('enter first number a :- '))
b=int(input('enter secound number b :- '))
opt=input('enter operator:- ')
if opt=='*' :
    d=a*b
    print('the result is', d )
elif opt == '/':
    d=a/b
    print('the result is', d )
elif opt == 'sq rt of a':
    d=math.sqrt(a)
    print('the result is', d )
elif opt == 'sq rt of b':
    d=math.sqrt(b)
    print('the result is', d )
elif opt == 'cube rt of a':
    d=a**(1/3)
    print('the result is', d )
elif opt == 'cube rt of b':
    d=b**(1/3)
    print('the result is', d )
elif opt == '+':
    d=a+b
    print('the result is', d )
elif opt == '-':
    d=a-b
    print('the result is', d )
elif opt == 'square of a':
    d=a*a   
    print('the result is', d )
elif opt == 'square of b':
    d=b*b
    print('the result is', d )
elif opt == 'cube of a':
    d=a*a*a
    print('the result is', d )
elif opt == 'cube of b':
    d=b*b*b
    print('the result is', d )
elif opt == 'a sq - b sq':
    d=(a*a)-(b*b)
    print('the result is', d )
elif opt == '(a+b)sq':
    d=(a+b)*(a+b)
    print('the result is', d )
elif opt == '(a+b)sq':
    d=(a-b)*(a-b)
    print('the result is', d )
elif opt == 'a sq + b sq':
    d=(a*a)+(b*b)
    print('the result is', d )
elif opt == 'a cube - b cube':
    d=(a*a*a)-(b*b*b)
    print('the result is', d )
elif opt == 'a cube + b cube':
    d=(a*a*a)+(b*b*b)
    print('the result is', d )
elif opt == '(a+b) cube':
    d=(a+b)*(a+b)*(a+b)
    print('the result is', d )
elif opt == '(a-b) cube':
    d=(a-b)*(a-b)*(a-b)
    print('the result is', d )
elif opt=='check remainder of a/b' or 'mod ofa/b' or 'mod a/b' :
    d=a % b
    print('the result is', d )
elif opt=='check remainder of b/a' or 'mod of b/a' or 'mod b/a' :
    d=b % a 
    print('the result is', d )
else:
 print('this is not a valid operator. contact the devloper for more info.')
 print("you can all the basic operators and square and cubic functions")
time.sleep(5)