def productSum(array, multiplier = 1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier +1)
		else:
			sum += element
	return sum * multiplier
#TC: O(n) where n is the TOTAL number of lements in the array and subarrays
#SC: O(D) where d is the depth which is the max multiplier in the subarrays
	
