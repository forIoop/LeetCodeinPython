#Write a function that turns a comma-delimited list into an array of strings.

#Examples
#to_array("watermelon, raspberry, orange")
#➞ ["watermelon", "raspberry", "orange"]

#to_array("x1, x2, x3, x4, x5")
#➞ ["x1", "x2", "x3", "x4", "x5"]

#to_array("a, b, c, d")
#➞ ["a", "b", "c", "d"]

#to_array("")
#➞ []
def to_array(txt):
	return txt.split(', ') if txt else []
