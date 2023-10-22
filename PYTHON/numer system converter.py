x=(input('enter the number:-'))
binary_string=bin(int(x))
b=oct(int(x))
c=hex(int(x))
print ("binary code of",x,"is",binary_string)
print ("octal code of",x,"is",b)
print ("hexadecimal code of",x,"is",c)
def dec(bin_str):
    try:
        decimal = int(bin_str,2)  
        print("The decimal value is :", decimal)    
    
    except ValueError:
        print("Invalid binary number")
import time
time.sleep(2)
dec(binary_string)