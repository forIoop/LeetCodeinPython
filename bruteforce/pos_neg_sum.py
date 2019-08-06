Positive Count / Negative Sum

Create a function that takes a list of positive and negative numbers. Return a list where the first element is the count of positive numbers and the second element is the sum of negative numbers.

Examples
sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]

sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]

sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]

sum_neg([]) ➞ []


def sum_neg(lst):
	if lst == []:
		return []
	output = []
	pos_list = []
	neg_list = []
	for i in range(len(lst)):
		if lst[i] > 0:
			pos_list.append(lst[i])
		else:
			neg_list.append(lst[i])
	output.append(len(pos_list))
	output.append(sum(neg_list))
	return output
