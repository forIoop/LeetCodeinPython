def hacker_speak(txt):
	hack = {'a': '4', 'e':'3', 'i':'1', 'o':'0','s':'5'}
	
	new_str = ''
	
	for ch in txt:
		if ch in hack:
			new_str += hack[ch]
		else:
			new_str += ch
	return new_str
