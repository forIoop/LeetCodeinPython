Calculate the Min Max len and avg of a list

def minMaxLengthAverage(lst):
	output = []
	output.append(min(lst))
	output.append(max(lst))
	output.append(len(lst))
	
	average = sum(lst) / len(lst)
	
	output.append(average)
	
	return output
	
