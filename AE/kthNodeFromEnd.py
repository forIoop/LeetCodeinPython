def removeKthNodeFromEnd(head, k):
	#Counter used to see how much we traverse second pointer
	counter = 1
	#Two pointer method
	first = head
	second = head
	# Traverse second node k times according to counter
	while counter <= k:
		second = second.next
		counter += 1
		
	# Case where we have to remove the root node update head
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	#Keep traversing both pointers until second.next is null
	while second.next is not None:
		second = second.next
		first = first.next
	#now update the next first pointer to its next next to throw in garbage collection
	first.next = first.next.next
  
  O(n) time | O(1) space
