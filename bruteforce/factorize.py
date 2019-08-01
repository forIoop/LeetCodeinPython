Create a function that takes a number as its argument and returns a list of all its factors.

Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]

factorize(4) ➞ [1, 2, 4]

factorize(17) ➞ [1, 17]

def factorize(num):
	factors = []
	for i in range(1,num):
		if num % i == 0:
			factors.append(i)
	factors.append(num)
	return factors
		
