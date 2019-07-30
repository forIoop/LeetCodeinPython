iven a list, transform it into a mirror.

Examples
mirror([0, 2, 4, 6]) ➞ [0, 2, 4, 6, 4, 2, 0]

mirror([1, 2, 3, 4, 5]) ➞ [1, 2, 3, 4, 5, 4, 3, 2, 1]

mirror([3, 5, 6, 7, 8]) ➞ [3, 5, 6, 7, 8, 7, 6, 5, 3]

def mirror(lst):
	mirror = []
	for i in range(len(lst)-2,-1,-1):
		mirror.append(lst[i])
	
	output = lst + mirror
	return output
	
