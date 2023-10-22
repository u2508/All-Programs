# Taking binary input
binary = input("Enter a binary number:")
decimal=0
l = len(binary)
 
#loop through each digit of binary
for x in binary:
    
    l = l-1
    decimal +=float( pow(2,l) * float(x) )  
print("Decimal of {p} is {q} ".format(p=binary, q=decimal))
import time
time.sleep(5)