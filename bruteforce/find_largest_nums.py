Create a function that takes a list of lists with integers or floats. Return a new (single) list with the largest numbers from each.

def findLargestNums(lst):
	max_element_list = []
	for sublist in lst:
		max_element_list.append(max(sublist))
		
	return max_element_list
