def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendantDepth(descendantOne, topAncestor)
	depthTwo = getDescendantDepth(descendantOne, topAncestor)
	if depthOne > depthTwo:
		return backtrackAncestralTree(descendantOne, decendantTwo, depthOne - depthTwo)
	else:
		return backtrackAncestralTree(descendantTwo, decendantOne, depthTwo - depthOne)
	
def getDescendantDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
		diff -= 1
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	
	return lowerDescendant
# O(D) time where D is the depth of the deeper of two descendants
# O(1) space, we are just iterating and not adding any more space / memory
