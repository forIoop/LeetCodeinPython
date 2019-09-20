def maxSubsetSumNoAdjacent(array):
	if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	maxSums = array[:]
	maxSums = max(array[0],array[1])
	for i in range(2,len(array)):
		maxSums[i] = max(maxSums[i-1], max[i - 2] + array[i])
	return maxSums[-1]
