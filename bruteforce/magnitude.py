You will be implementing a basic case of the map-reduce pattern in programming. Given a vector stored as a list of integers, find the magnitude of the vector. Use the standard distance formula for n-dimensional Cartesian coordinates.

Examples
magnitude([3, 4]) ➞ 5

magnitude([0, 0, -10]) ➞ 10

magnitude([]) ➞ 0

magnitude([2, 3, 6, 1, 8] ) ➞ 10.677078252031311

import math

def magnitude(lst):
    sum_of_squares = 0
    for element in lst:
		    sum_of_squares += element ** 2
    return math.sqrt(sum_of_squares)
