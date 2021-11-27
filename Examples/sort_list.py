#!/usr/bin/env python3

s_list = [1, 4, 6, 3, 2, 8, 9, 7, 5, 3, 2, 3, 4]



def sort_lst(lst, order):
	""" Sort the provided list by the defined order.

	lst - List Array of numeric values to be sorted.
	order - asc, desc, none(Will return original list)
	"""
	if order.upper == "NONE":
		return lst

	# Sort our list <-> numerically
	lst.sort()

	# Default order is ASC
	if order.upper() == "ASC":
		return lst
	
	# Reverse our order
	elif order.upper() == "DESC":
		lst.reverse()
		return lst

	# Unhandled Exception
	else:
		return False



print("Unordered list = ", end="")
print(s_list)

print("Ordered list = ", end="")
print(sort_lst(s_list, "asc"))
