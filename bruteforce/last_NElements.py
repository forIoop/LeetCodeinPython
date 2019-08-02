def last(a, n):
	if n == 0:
		return []
	if n > len(a):
		return "invalid"
	else:
		return a[len(a) - n:]
