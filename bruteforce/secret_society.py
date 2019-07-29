A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.

def society_name(friends):
	friends.sort()
	codename = []
	for i in range(len(friends)):
		codename.append(friends[i][0])
	
	
	s = "".join(codename)
	return s
