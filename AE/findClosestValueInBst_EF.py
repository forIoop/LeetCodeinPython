def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree,target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target-closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left,target,closest)
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right,target,closest)
	else:
		return closest

	#TC: Average case of O(log(n)) time | worst case time of O(n)
	#SC: Average case of O(1) | Worst case of O(1)
