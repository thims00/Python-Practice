#!/usr/bin/env python3


# Get a number from the user and tell them if the number
# is greater then 10 or not.


import sys


# Ask our user for a number and store it as user_nmbr
user_nmbr = input("Enter a number: ")




# If user_nmbr IS NOT a number, let our user know and exit
if not user_nmbr.isnumeric():
	print("ERROR: That input is not a number.")
	
	# Exit our program with an error (status greater than 0)
	sys.exit(1)


# Default Condition #
# If our input IS numeric then decide if above or below 10
else:
	if user_nmbr < 10:
		print("Number is less than 10!")
	
	elif user_nmbr == 10:
		print("Number is 10!")

	else:
		print("Number is greater than 10")


# Exit our program successfully
sys.exit(0)
