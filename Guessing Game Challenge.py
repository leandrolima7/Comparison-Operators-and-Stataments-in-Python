#importing the method randint from the class random
from random import randint 
#importing system method from OS
from os import system
#importing system method from OS
from time import sleep
#print the rules
print("Rules:")
print("1 - If a player's guess is less than 1 or greater than 100, you'll get 'OUT OF BOUNDS' message")
print("2 - On a player's first turn, if their guess is\n\twithin 10 of the number, you'll get 'WARM!'\n\tfurther than 10 away from the number, you'll get 'COLD!' ")
print("3 - On all subsequent turns, if a guess is:\n\tcloser to the number than the previous guess you'll get 'WARMER!'\n\tfarther from the number than the previous guess, you'll get 'COLDER!")
print("4 -  When the player's guess equals the number, you'll get 'Correctly' and how many guesses it took!")

print("After reading the rules, press Enter key to continue!")

while True:
	#This if condition checks wheter the user pressed Enter key or not
	if input() == "":
		system('cls')
		break
	else:
		print("Input not valid! Please press Enter Key")

#Getting the number to be guessed
number = randint(0,10)

#Getting players
players = int(input("Type the number of players:"))

names = []

for i in range(0,players):
	names.append(input(f"Name of player number {i+1}: ")) 

print("Loading...")
sleep(1)
system('cls')

#List to save the guesses of each player
guessed = []
for i in range(0,players):
	guessed.append(0) 
print(number)
#First turn
for i in range(0,players):
	while True:
		guessed[i] = int(input(f"{names[i]}, the number is: ")) 
		if guessed[i] < 1 or guessed[i] > 100:
			print("OUT OF BOUNDS! Your guess must be placed beetwen 1 and 100\nPlease, try it again!")
			while True:
				print("Press Enter key to try agian")
				if input() == "":
					sleep(1)
					system('cls')
					break
				else:
					print("Input not valid! Please press Enter Key")
					sleep(3)
					system('cls')
		else:
			break
			
	guessed_actual = guessed[i]
	if guessed[i] == number:
		print(f"{names[i]}, you guessed Correctly! It took 1 guess!")
		break
	elif abs(number-guessed[i]) <= 10:
		print(f"{names[i]}, you guess is WARM!")
	else:
		print(f"{names[i]}, you guess is COLD!")
	print("Loading...")
	sleep(3)
	system('cls')

#List to save the number of guesses of each player
number_of_guesses = []
for i in range(0,players):
	number_of_guesses.append(1) 

#Guessing game
while(guessed_actual != number):
	for i in range(0,players):
		print(f"{names[i]} your last guess was: {guessed[i]}\nUntil now you have guessed {number_of_guesses[i]} times!")
		guessed_actual = int(input(f"{names[i]}, the number is: ")) 
		number_of_guesses[i] += 1;
		if guessed_actual == number:
			print(f"{names[i]} you guessed Correctly! It took {number_of_guesses[i]} guesses!")
			break
		elif abs(number-guessed_actual) < abs(number-guessed[i]):
			print(f"{names[i]} you guess is WARMER then the previous guess!")
		else:
			print(f"{names[i]} you guess is COLDER then the previous guess!")
		guessed[i] = guessed_actual
		print("Loading...")
		sleep(3)
		system('cls')

