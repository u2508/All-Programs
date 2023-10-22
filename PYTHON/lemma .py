# program to find dividend
a=int (input('enter divisor:-'))
n=int (input('enter quotient:-'))
c=int (input('enter remainder:-'))

def f1(b,q,r):
    d=b*q+r
    if (r >= b):
        print ("remainder can't be greater or equal to divisor")

    elif (r==0):
        print ("Applying Euclid's lemma the dividend is",d)
        print (d,'is divisible by',b)
    elif(r<0):
        
        print("remainber should not be negative")
        print ("But,Applying Euclid's lemma the dividend is",d)           
    else:
        
        print ('Applying Euclids lemma the dividend is',d)
        print (d,'is not divisible by',b)
f1(a,n,c)
import time
time.sleep(2)