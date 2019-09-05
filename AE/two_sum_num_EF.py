def twoNumberSum(array, targetSum):
	ht = dict()
	for i in range(len(array)):
		y = targetSum - array[i]
		if y in ht:
			return sorted([array[i],y]) 
		else:
			ht[array[i]] = "True"
	return []
							   
