def closestValueInBst(tree, target):
    return self.findClosestValueInBSTHelper(tree, target, float("inf"))


def findClosestValueInBSTHelper(node,target, closest):
    if node is None:
        return closest

    if abs(target - closest) > abs(target - node.value):
        closest = node.value
    
    if target < node.value:
        return self.findClosestInBSTHelper(node.left, target,closest)
    
    elif target > tree.value:
        return self.findClosestValueInBSTHelper(node.right,target,closest)
    
    else:
        return closest
