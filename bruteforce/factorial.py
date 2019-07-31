#given a number Z, return the factorial of that number
def factorial(Z):
	if Z == 0:
		return 1
	else:
		return Z * factorial(Z-1)
	
