Create a function that takes a number (step) as an argument and returns the amount of matchsticks in that step. See step 1, 2 and 3 in the image above.

Examples
match_houses(1) ➞ 6

match_houses(4) ➞ 21

match_houses(87) ➞ 436

def match_houses(step):
	if step == 0:
		return 0
	
	if step <= 1:
		return 6
	else:
		return 5 + match_houses(step-1)
	
