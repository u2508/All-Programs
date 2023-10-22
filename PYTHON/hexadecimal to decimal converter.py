# Python Program - Convert Hexadecimal to Decimal
def dec(hex='0x0'):
    dec = int(hex, 16)
    y=str(dec)
    print(hex,"in Decimal =",y)
    return dec
print("Enter 'x' for closing the program.")
x=str(input("Enter number in Hexadecimal Format: "))
hexa = '0x'+ x
if x == 'x':
    exit()
elif x =='':
    dec()
else:
    x=dec(hexa)
import time
time.sleep(0.1*x)