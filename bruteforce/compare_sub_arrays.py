Two sisters are eating chocolate, whose pieces are represented as subarrays of [l x w].

Write a function that returns True if the total area of chocolate is the same for each sister.

To illustrate:

test_fairness([[4, 3], [2, 4], [1, 2]],
[[6, 2], [4, 2], [1, 1], [1, 1]])
➞ True

// Agatha's pieces: [4, 3], [2, 4], [1, 2]
// Bertha's pieces: [6, 2], [4, 2], [1, 1], [1, 1]

// Total area of Agatha's chocolate
// 4x3 + 2x4 + 1x2 = 12 + 8 + 2 = 22

// Total area of Bertha's chocolate is:
// 6x2 + 4x2 + 1x1 + 1x1 = 12 + 8 + 1 + 1 = 22

def test_fairness(agatha, bertha):
	suma = 0
	sumb = 0
	for x in agatha:
		suma += x[0]*x[1]
	for x in bertha:
		sumb += x[0]*x[1]
	if(suma == sumb):
		return True
	return False
