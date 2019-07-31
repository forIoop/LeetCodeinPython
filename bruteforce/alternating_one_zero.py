Write a function that returns True if the binary string can be rearranged to form a string of alternating 0s and 1s.

Examples
can_alternate("0001111") ➞ True
# Can make: "1010101"

can_alternate("01001") ➞ True
# Can make: "01010"

can_alternate("010001") ➞ False

can_alternate("1111") ➞ False

def can_alternate(s):
	if '1' not in s or '0' not in s:
		return False
		
	else:
		zero_count = 0
		one_count = 0
		for i in range(len(s)):
			if s[i] == '0':
				zero_count += 1
			else:
				one_count += 1
		if abs(zero_count - one_count) == 1 or abs(zero_count - one_count) == 0:
			return True
		else:
			return False
