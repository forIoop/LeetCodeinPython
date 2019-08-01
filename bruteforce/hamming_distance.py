Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.

def hamming_distance(txt1, txt2):
	count = 0
	for i in range(len(txt1)):
		if txt1[i] != txt2[i]:
			count += 1
	return count
