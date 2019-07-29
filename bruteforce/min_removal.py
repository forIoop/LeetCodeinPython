Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.

Examples
minimum_removals([1, 2, 3, 4, 5]) ➞ 1

minimum_removals([5, 7, 9, 11]) ➞ 0

minimum_removals([5, 7, 9, 12]) ➞ 1

def minimum_removals(lst):
	sum = 0
	for i in range(len(lst)):
		sum += lst[i]
	if sum % 2 == 0:
		return 0
	else:
		return 1
		
	
