Create a function to count the number of 1s in a 2D list.

def count_ones(matrix):
	count = 0
	for sublist in matrix:
		for i in range(len(sublist)):
			if sublist[i] == 1:
				count += 1
	return count
		
	
