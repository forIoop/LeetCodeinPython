# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

	#O(n) time and O(1) space
    def buildHeap(self, array):
		firstParentIdx = (len(array) - 2) // 2
		for currentIdx in reversed(range(firstParentIdx)):
			self.siftDown(currentIdx, len(array)-1, array)
		return array
		
	#Olog(n) time and O(1) space	
    def siftDown(self, currentIdx, endIdx, heap):
    	childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[indexToSwap] < heap[currentIdx]
				self.swap(indexToSwap, currentIdx, heap)
				currentIdx = indexToSwap
				childOne Idx = currentIdx * 2 + 1
			else:
				break
	# O log(n) time and O(1) space
    def siftUp(self, currentIdx,heap):
    	parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]: 
			self.swap(currentIdx,parfentIdx,heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
			
	

    def peek(self):
    	return self.heap[0]

    def remove(self):
    	swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0,len(self.heap)-1, self.heap)
		return valueToRemove
		

    def insert(self, value):
    	self.heap.append(value)
		self.siftUp(len(self.heap)-1, self.heap)
		
	def swap(self, i,j heap):
		heap[i], heap[j] = heap[j], heap[i]
		
