Create a function that returns the index of the first vowel in a string.

Examples
first_vowel("apple") ➞ 0

first_vowel("hello") ➞ 1

first_vowel("STRAWBERRY") ➞ 3

first_vowel("pInEaPPLe") ➞ 1

def first_vowel(txt):
	vowels = ['a','A','e','E','i','I','o','O','u','U']
	for i in range(len(txt)):
		if txt[i] in vowels:
			return i
	
