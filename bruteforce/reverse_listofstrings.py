Write a function that reverses all the words in a sentence starting with a particular letter.

def special_reverse(s, c):
	words_list = s.split()
	output_list = []
	for word in words_list:
		if word[0] == c:
			output_list.append(word[::-1])
		else:
			output_list.append(word)
			
	output = ' '.join(output_list)
	return output
	
	
