def char_index(word, char):

	
	output = []
	last_index = 0
	for i in range(len(word)):
		if char not in word:
			return None
		else:
			if word[i] == char and i not in output:
				output.append(i)
	
	new_list = []
	new_list.append(output[0])
	new_list.append(output[len(output)-1])
	return new_list
