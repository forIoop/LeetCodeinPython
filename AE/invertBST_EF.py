def invertBinaryTree(tree):
	if tree is None:
		return 
	
	swapLeftAndRight(tree)
	invertBinaryTree(tree.left)
	invertBinarytree(tree.right)

def swapLeftAndRight(tree)
	tree.left, tree.right = tree.right, tree.left
		
#O(n) time
#O(d) space
