#!/usr/bin/env python3


""" Define a list and iterate over the list for display. """

# Import our sys module to allow for clean program exit
import sys


# Define our list 
data_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]



# Let the user know what is going on
print("The list information: ")

for data in range(len(data_list)):
	### Add formatting and print our data
	# Insert 4 spaces and a -, without a \newline
	print("    - ", end="")
	# Output our data to finish the line`
	print(data_list[data])



# Cleanly exit our program with a True return status
sys.exit(0)
