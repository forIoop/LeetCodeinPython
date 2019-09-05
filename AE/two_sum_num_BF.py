def twoNumberSum(array, targetSum):
	lst = []
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i] + array[j] == targetSum:
				lst.append(array[i])
				lst.append(array[j])
				return sorted(lst)
	return []
