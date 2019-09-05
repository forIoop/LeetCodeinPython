def twoNumberSum(array, targetSum):
	ht = dict()
	for i in range(len(array)):
		potentialMatch = targetSum - array[i]
		if potentialMatch in ht:
			return [potentialMatch,array[i] 
		else:
			ht[array[i]] = True
	return []
							   
#TC: O(N)
#SC: O(N)
