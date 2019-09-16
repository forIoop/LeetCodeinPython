
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = array[idxOne]
		secondNum = array[idxTwo]
		
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = secondNum - firstNum
			idxtwo += 1
		
		else:
			return[firstNum,secondNum]
		
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]

	return smallestPair
#Time = O(Nlog(N) + Mlog(M))
#Space = O(1)
