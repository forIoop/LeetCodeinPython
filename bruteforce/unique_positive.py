def unique_lst(lst):
	output = []
	for i in range(len(lst)):
		if lst[i] > 0 and lst[i] not in output:
			output.append(lst[i])
	return output
			
