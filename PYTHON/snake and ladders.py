import random,time
player1 = 0

player2 = 0



a = range(1,11);b = range(11,21)[::-1];c = range(21,31);d = range(31,41)[::-1];e = range(41,51);f = range(51,61)[::-1];g = range(61,71);

h = range(71,81)[::-1];i = range(81,91);j = range(91,101)[::-1]

print ("Snakes and Ladders game")

print (j,'\n',i,'\n',h,'\n',g,'\n',f,'\n',e,'\n',d,'\n',c,'\n',b,'\n',a)



def check_for_snakes_and_ladders(n):

	"""This method checks for the presence of snakes or ladders in the board"""

	ladders = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:100}

	snakes = {98:78,95:75,93:73,87:24,64:60,62:19,56:53,49:11,48:26,16:6}
	print ('ladders are',ladders)
	print ('snakes are',snakes)
	if n in ladders:

		print ("Its a ladder,Climb up")

		n = ladders[n]

	elif n in snakes:

		print ("Its a snake!!,Come down")

		n = snakes[n]

	return n





def roll_dice(r):
    d=random.randint(1,6)
    print ("The values of dice is ",d)
    d = r + d
    return d
while player1 < 100 or player2 < 100:

	print ("Its turn of player1\n")

	player1 = roll_dice(player1)

	player1 = check_for_snakes_and_ladders(player1)

	print ("Current status of Player1:",player1,"and Player2:",player2)

	time.sleep(6)

	if player1 > 99:

		print ("Winner of the game is player1")
		time.sleep(5)
		break



	print ("Its turn of player2\n")

	player2 = roll_dice(player2)

	player2 = check_for_snakes_and_ladders(player2)

	print ("Current status of Player1:",player1," and Player2:",player2)
	time.sleep(6)


	if player2 > 99:

		print ("Winner of the game is player2")
		time.sleep(5)
		break