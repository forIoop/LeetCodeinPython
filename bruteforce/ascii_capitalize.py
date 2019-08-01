Create a function that takes a string as input and capitalizes a letter if it's ASCII code is even,
and returns its lower case version if it's ASCII code is odd.

def ascii_capitalize(txt):
	output = ""
	for i in txt:
		if ord(i) % 2 == 0:
			output = output + i.upper()
		else:
			output = output + i.lower()
	return output
