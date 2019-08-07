
#Create a function that takes a string and returns the number of alphanumeric characters that occur more than once.
def duplicate_count(txt):
	sum = 0
  for i in txt:
  	if txt.count(i) >= 2:
    	sum += 1
  return sum
