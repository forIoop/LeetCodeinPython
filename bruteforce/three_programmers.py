You hired three programmers and you (hopefully) pay them. Create a function that takes three numbers (the hourly wage of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.

Examples
programmers(147, 33, 526) ➞ 493

programmers(33, 72, 74) ➞ 41

programmers(1, 5, 9) ➞ 8

def programmers(one, two, three):
	array = []
	array.append(one)
	array.append(two)
	array.append(three)
	
	sorted_list = sorted(array)
	return sorted_list[len(sorted_list)-1] - sorted_list[0]
	
