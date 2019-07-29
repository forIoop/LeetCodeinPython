Create a function that returns the total number of parameters passed in.

Examples
number_args("a", "b", "c") ➞ 3

number_args(10, 20, 30, 40, 50) ➞ 5

number_args(x, y) ➞ 2

number_args() ➞ 0

def number_args(*args):
	return len(args)
