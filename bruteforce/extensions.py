Write a function that maps files to their extension names.

Examples
get_extension(["code.html", "code.css"])
➞ ["html", "css"]

get_extension(["project1.jpg", "project1.pdf", "project1.mp3"])
➞ ["jpg", "pdf", "mp3"]

get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"])
➞ ["rb", "cpp", "py", "js"]


def get_extension(lst):
	split_list = []
	for i in lst:
		split_list.append(i.split('.'))
		
	extensions = []
	for i in range(len(split_list)):
		extensions.append(split_list[i][1])
	return extensions
	
		
