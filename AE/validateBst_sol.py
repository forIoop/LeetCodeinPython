def validateBst(tree):
	return validateBstHelper(tree, float("-inf"),float("inf"))

def validateBstHelper(tree, minValue, maxvalue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	leftisValid = validateBstHelper(tree.left, minValue, tree.value)
	return leftisValid and validateBstHelper(tree.right, tree.value, maxValue)
	
	#TC: O(n)
  #SC: O(d) where d is the max depth of the binary tree
