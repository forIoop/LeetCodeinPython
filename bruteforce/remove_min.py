Create a function that takes a list of integers and removes the smallest value.

def remove_smallest(lst):
	if lst == []:
		return lst
	min_removed = []
	min_element = lst[0]
	for i in range(len(lst)):
		if lst[i] < min_element:
			min_element = lst[i]
	lst.remove(min_element)
	
	return lst
		
