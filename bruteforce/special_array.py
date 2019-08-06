def is_special_array(lst):
	for i in range(len(lst)):
			if i % 2 == 0:
				if lst[i] % 2 != 0:
					return False
			else:
				if lst[i] % 2 != 1:
					return False
	return True
