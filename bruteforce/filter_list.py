def filter_list(lst):
	only_ints = []
	for i in range(len(lst)):
		if type(lst[i]) == int:
			only_ints.append(lst[i])
	return only_ints
		
