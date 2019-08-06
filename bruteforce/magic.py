You are to read each part of the date into its own integer type variable. The year should be a 4 digit number. You can assume the user enters a correct date (no error checking required).

Determine whether the entered date is a magic date. Here are the rules for a magic date:

mm * dd is a 1-digit number that matches the last digit of yyyy or
mm * dd is a 2-digit number that matches the last 2 digits of yyyy or
mm * dd is a 3-digit number that matches the last 3 digits of yyyy

def magic(txt):
	m, d, y = txt.split()
	return y.endswith(str(int(m) * int(d)))
