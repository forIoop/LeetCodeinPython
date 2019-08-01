Create a function that takes an array of numbers and return its median. If the input array is even length, take the average of the two medians, else, take the single median.

Examples
median([2, 5, 6, 2, 6, 3, 4]) ➞ 4

median([21.4323, 432.54, 432.3, 542.4567]) ➞ 432.4

median([-23, -43, -29, -53, -67]) ➞ -43

def median(lst):
	sorted_list = sorted(lst)
	median = 0
	if len(sorted_list) % 2 == 0:
		first = sorted_list[len(sorted_list) // 2 - 1]
		second = sorted_list[len(sorted_list) // 2 ] 
		medium = (first+second)/2
		return medium
	else:
		return sorted_list[len(sorted_list) // 2]
