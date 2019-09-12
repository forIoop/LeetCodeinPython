def bubbleSort(array):
	counter = 0
	for i in range(len(array)-1 - counter):
		for j in range(i+1,len(array)):
			if array[i] > array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
		counter += 1
	return array
