int charCount(char myChar, std::string str) {
	int count = 0;
	for(int i = 0; i < str.length(); i++) {
		if (str[i] == myChar) {
			count += 1;
		}
	}
	return count;
}
