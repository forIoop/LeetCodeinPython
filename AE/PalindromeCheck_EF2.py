def isPalindrome(string, i = 0):
	j = len(string) - 1 - i
	if i >= j:
		return True
	if string[i] != string[j]:
		return False
	return isPalindrome(string, i+1)
#O(n) time and O(n) space 
