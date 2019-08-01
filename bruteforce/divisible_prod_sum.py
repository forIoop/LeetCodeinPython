Write a function that returns true if the product of a list is divisible by the sum of that same list.

Examples
divisible[3, 2, 4, 2] ➞ false

divisible[4, 2, 6] ➞ true

divisible[3, 5, 1] ➞ false

def divisible(lst):
	product = 1
	for i in lst:
		product *= i
	
	if product % sum(lst) == 0:
		return True
	
	else:
		return False
	
