def letter_check(lst):
	string_one = lst[0]
	string_two = lst[1]
	for i in range(len(string_two)):
		if string_two[i].lower() not in string_one.lower():
			return False
	return True
	
