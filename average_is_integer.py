# check if the average of a list is a whole number
def is_avg_whole(arr):
	return (sum(arr) / len(arr)).is_integer()
