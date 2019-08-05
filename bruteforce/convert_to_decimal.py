Create a function to convert a list of percentages to their decimal equivalents.

def convert_to_decimal(perc):
	stripped_list = []
	for i in range(len(perc)):
		stripped_list.append(perc[i].strip('%'))
	
	decimal_list = []
	for i in range(len(stripped_list)):
		decimal_list.append(float(stripped_list[i]) / 100)
	return decimal_list
