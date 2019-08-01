def is_palindrome(n):
	original = n
	rev = 0
	d = 0
	while n > 0:
		d = n % 10
		n = int(n / 10)
		rev = rev * 10 + d
	if rev == original:
		return True
	else:
		return False
	
