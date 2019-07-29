def subset(lst1, lst2):
	lst2_set = set(lst2)
	return set(lst1).issubset(lst2)
	
  Create a function that determines with the first list is a subset of the second.

Examples
subset([1, 3], [1, 3, 3, 5]) ➞ True

subset([4, 8, 7], [7, 4, 4, 4, 9, 8]) ➞ True

subset([1, 3], [1, 33]) ➞ False

subset([1, 3, 10], [10, 8, 8, 8]) ➞ False
