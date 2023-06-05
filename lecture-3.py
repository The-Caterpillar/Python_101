import random

print("Let's begin the game")

y = 1

while(y==1):
	r = random.randint(1,20)
	print("\nEnter a random number")

	while(True):
		x = int(input())
		if(x<r):
			print("Wrong guess, try a greater number")
		elif(x>r):
			print("Wrong guess, try a smaller number")
		else:
			print("Congrats, you got the number")
			break;
	
	print("\n If you wish to continue the game press 1 else press 0: ")
	y = int(input())