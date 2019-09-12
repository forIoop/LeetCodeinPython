def isPalindrome(string):
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString
# O(n^2) time | O(n) space
