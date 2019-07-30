Create a function that returns the total number of steps it takes to transform each element 
to the maximal element in the list. Each step consists of incrementing a digit by one.

def increment_to_top(lst):
	max_num = 0
	for i in range(len(lst)):
		if lst[i] > max_num:
			max_num = lst[i]
			
	increment = []
	for i in range(len(lst)):
		increment.append(max_num-lst[i])
	
	return sum(increment)
