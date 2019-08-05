Write a function that takes three arguments (x, y, z) and returns a list containing sublists (e.g. [[], [], []]), each of a certain number of items, all set to either a string or an integer.

x argument: Number of sublists contained within the main list.
y argument Number of items contained within each sublist(s).
z argument: Item contained within each sublist(s).

def matrix(x, y, z):
	sublist = []
	for i in range(y):
		sublist.append(z)
	
	main_list = []
	for i in range(x):
		main_list.append(sublist)
	
	return main_list
