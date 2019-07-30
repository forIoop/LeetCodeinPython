Write a function that returns the lexicographically first and lexicographically last rearrangements of a string. Output the results in the following manner:

first_and_last(string) ➞ [first, last]
Examples
first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]

first_and_last("bench") ➞ ["bcehn", "nhecb"]

first_and_last("scoop") ➞ ["coops", "spooc"]

def first_and_last(s):
	s_list = []
	output = []
	for i in range(len(s)):
		s_list.append(s[i])
	
	sorted_list = sorted(s_list)
	sorted_list_rev = []
	
	for i in range(len(sorted_list)-1,-1,-1):
		sorted_list_rev.append(sorted_list[i])
	
	sorted_string = ''.join(sorted_list)
	sorted_rev_string = ''.join(sorted_list_rev)
	output.append(sorted_string)
	output.append(sorted_rev_string)
	return output
	
		
	
