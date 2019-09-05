def twoNumberSum(array, targetSum):
	lst = []
	for i in range(len(array)-1):
		firstNum = array[i]
		for j in range(i+1,len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []
#TC: O(N^2)
#SC: O(1)
