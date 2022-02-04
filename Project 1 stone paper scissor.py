#Game stone paper scissor

import random

user_win = 0
comp_win = 0

option = ["stone", "paper", "scissor"]

while True:
	print(" ")

	user_input =  input("Enter your choice - ")
	print("Your choice is: " ,user_input)

	if user_input == "exit":
		break

	if user_input in option:
		print("Correct option")
		comp_input = random.choice(option)
		print("Computer option is: ", comp_input)

		if user_input == comp_input:
			print("____Tie____")

		elif user_input == "stone" and comp_input == "scissor":
			user_win = user_win + 1
			print("---User won---")

		elif user_input == "paper" and comp_input == "stone":
			user_win = user_win + 1
			print("---User won---")

		elif user_input == "scissor" and comp_input == "paper":
			user_win = user_win + 1
			print("---User won---")
		else:
			comp_win = comp_win + 1
			print("*#%@* User lost *#%@*")
	else:
		print("Incorrect option")

print("Game over")
print("User score is: " ,user_win)
print("Computer score is: " ,comp_win)
