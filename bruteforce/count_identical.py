Identical Sublists
Create a function that takes in a two-dimensional list and returns the number of sub-lists with identical elements.

def count_identical(lst):
	count=0
	for i in lst:
		if len(set(i))==1:
			count+=1
	return count
