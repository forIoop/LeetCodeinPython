Create a function that moves all capital letters to the front of a word.

Examples
cap_to_front("hApPy") ➞ "APhpy"

cap_to_front("moveMENT") ➞ "MENTmove"

cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

def cap_to_front(s):
	upper_list = []
	lower_list = []
	output = []
	for i in s:
		if i.isupper():
			upper_list.append(i)
		else:
			lower_list.append(i)
	
	output_list = upper_list + lower_list
	output = ''.join(output_list)
	return output
	
			
			
