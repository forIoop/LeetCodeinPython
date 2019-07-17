#in semantic versioning a piece of software can be represented in a format like this example: 6.1.9.

#The first number is the major version.
#The second number is the minor version.
#The third number is the patch (bug fixes).
#Create three separate functions, one to retrieve each element in the semantic versioning specification.

#Examples
# 6.1.9
#retrieve_major("6.1.9") ➞ "6"

#retrieve_minor("6.1.9") ➞ "1"

#retrieve_patch("6.1.9") ➞ "9"

# 2.1.0
#retrieve_major("2.1.0") ➞ "2"

#etrieve_minor("2.1.0") ➞ "1"

#retrieve_patch("2.1.0") ➞ "0"


def retrieve_major(semver):
	return semver.split('.')[0]

def retrieve_minor(semver):
	return semver.split('.')[1]	

def retrieve_patch(semver):
	return semver.split('.')[2]
