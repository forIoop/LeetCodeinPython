def maskify(txt):
	if len(txt) < 4:
		return txt
	else:
		output = []
		for i in range(3,len(txt)-1):
			output.append("#")
		return ''.join(output) + txt[len(txt)-4:len(txt)]
