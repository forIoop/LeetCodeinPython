Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.

def sum_two_smallest_nums(lst):
	pos_list = []
	for i in range(len(lst)):
		if lst[i] < 0:
			continue
		else:
			pos_list.append(lst[i])
			
	return sorted(pos_list)[0] + sorted(pos_list)[1]
		
