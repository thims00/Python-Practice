#!/usr/bin/env python3

s_list = [1, 4, 6, 3, 2, 8, 9, 7, 5, 3, 2, 3, 4]



def sort_lst(lst, order):
	""" Sort the provided list by the defined order.

	lst - List Array of numeric values to be sorted.
	order - asc, desc, none(Will return original list)
	"""
	if order.upper == "NONE":
		return lst


	lst.sort()

	if order.upper() == "ASC":
		return lst

	elif order.upper() == "DESC":
		lst.reverse()
		return lst
	else:
		return False



print("Unordered list = ", end="")
print(s_list)

print("Ordered list = ", end="")
print(sort_lst(s_list, "asc"))
