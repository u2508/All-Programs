decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal  #copying number
 
#calculating binary
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
       
print("Binary of {x} is: {y}".format(x=decimal,y=binary))
import time
time.sleep(5)