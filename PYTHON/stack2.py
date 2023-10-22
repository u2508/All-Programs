# Write a python program to check whether a string is a palindrome or not using stack.
stack = []
top = -1
# push function
def push(ele):
    global top
    top += 1
    stack[top] = ele
# pop function
def pop():
    global top
    ele = stack[top]
    top -= 1
    return ele
# Function that returns 1 if string is a palindrome
def isPalindrome(string):
    global stack
    length = len(string)
# Allocating the memory for the stack
    stack = ['0'] * (length + 1)
    # Finding the mid
    mid = length // 2
    i = 0
    while i < mid:
        push(string[i])
        i += 1
# Checking if the length of the string is odd, if odd then neglect the middle character
    if length % 2 != 0:
        i += 1
# While not the end of the string
    while i < length:
        ele = pop()
# If the characters differ then the given string is not a palindrome
        if ele != string[i]:
            return False
        i += 1
    return True
string = input("Enter string to check:")
if isPalindrome(string):
        print("Yes, the string is a palindrome")
else:
        print("No, the string is not a palindrome")