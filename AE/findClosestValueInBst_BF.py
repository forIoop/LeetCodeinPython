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
#TC: Average of O(Log(n)) | Worst case of O(N)
#SC: Average of O(Log(n)) | Worst case of O(N)
	
	
		
