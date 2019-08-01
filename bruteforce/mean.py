#given a list of numbers, calculate the mean rounded to one decimal place
def mean(nums):
	return round(sum(nums)/len(nums),1)
