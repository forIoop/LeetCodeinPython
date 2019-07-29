Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

To illustrate:

largest_swap(27) ➞ False

largest_swap(43) ➞ True

def largest_swap(num):
	original = num
	d = 0
	rev = 0
	while num > 0:
		d = num % 10
		num = int(num/10)
		rev = rev*10 + d
	if rev > original:
		return False
	else: 
		return True
		
	
