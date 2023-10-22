import random,time
n= random.randint(1,10)
guesses=0
for guesses in range(1,6): 
    guess = int(input("Enter an integer from 1 to 10: "))
    if (guess < n):
        print ("guess is low")
        print ("this is your guess %d "%guesses)
    elif (guess > n):
        print ("guess is high")
        print ("this is your guess %d " %guesses)
    elif (guess == n):
        guesses = (guesses)
        print ("You guess the number in", guesses , " guesses") 
        break  
if guess != n:
    n = str(n)
    print ("The secret number was",  n)
time.sleep(5)