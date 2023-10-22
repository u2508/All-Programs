octal = input('Enter a Octal number: ')
decimal = 0
 
#length of octal input
l = len(octal)
 
#loop through each digit of binary
for x in octal:
    
    l = l-1                        #decrease l by 1
    decimal += pow(8,l) * float(x)   #multiply
print("Decimal of {p} is {q} ".format(p=octal, q=decimal))
import time
time.sleep(5)