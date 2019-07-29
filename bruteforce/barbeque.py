You are in charge of the barbecue grill. A vegetarian skewer is a skewer that has only vegetables (-o). A non-vegetarian skewer is a skewer with at least one piece of meat (-x).

For example, the grill below has 4 non-vegetarian skewers and 1 vegetarian skewer (the one in the middle).

["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",
"--xx--x--ox--",
"--xx--x--ox--"]
Given a BBQ grill, write a function that returns [# vegetarian skewers, # non-vegarian skewers]. For example above, the function should return [1, 4].

def bbq_skewers(grill):
	veg = 0
	non_veg = 0
	lst = []
	for i in range(len(grill)):
		if "-" in grill[i] and "x" not in grill[i]:
			veg += 1
		else:
			non_veg += 1
		
	lst.append(veg)
	lst.append(non_veg)
	return lst
