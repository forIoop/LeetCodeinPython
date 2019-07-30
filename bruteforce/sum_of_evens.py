Create a function that returns the sum of all even elements in a 2D matrix.

def sum_of_evens(lst):
	sum = 0
	for i in range (len(lst)):
		for j in range (len(lst[i])):
			if (lst[i][j]%2==0):
				sum += lst[i][j]
	return sum
