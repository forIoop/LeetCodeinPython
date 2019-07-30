Create a function that filters out a list of state names into two categories based on the second parameter.

Abbreviations abb
Full names full

def filter_state_names(lst, cat):
	if cat == "abb":
		abb_list = []
		for i in range(len(lst)):
			if len(lst[i]) == 2:
				abb_list.append(lst[i])
		return abb_list
	else:
		full_list = []
		for i in range(len(lst)):
			if len(lst[i]) != 2:
				full_list.append(lst[i])
		return full_list
