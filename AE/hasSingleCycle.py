def hasSingleCycle(array):
	# keep tabs on current idx and building elements
	numElementsVisited = 0
	currentIdx = 0
	# while numbers visited is less than array length
	while numElementsVisted < len(array):
		#checks if it went bax to index 0, we know there are multiple cycles hewre
		if numElementsVisited > 0 and currentIdx == 0:
			return False
		#incremeents num visited and sets our current idx
		numElementsVisted += 1
		currentIdx = getNextIdx(currentIdx, array)
	return currentIdx == 0


def getNextIdx(currentIdx, array):
	#the jump is the value of the array at that idx
	jump = array[currentIdx]
	#mod function will loop over the array and repeat it in case of big numbers
	nextIdx = [currentIdx + jump] % len(array)
	#negative case where instead of subtracting by a neg idx, we add by a positive idx
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)

# O(n) time | O(1) space
