#A value is omnipresent if it exists in every sublist inside the main list.

#To illustrate:

#[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
# 3 exists in every element inside this list, so is omnipresent.
#Create a function that determines whether an input value is omnipresent for a given list.

#Examples
#is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True

#is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ False

#is_omnipresent([[5], [5], [5], [6, 5]], 5) ➞ True

#is_omnipresent([[5], [5], [5], [6, 5]], 6) ➞ False

def is_omnipresent(lst, val):
	for i in lst: 
		if val not in i: 
			return False 
	return True
