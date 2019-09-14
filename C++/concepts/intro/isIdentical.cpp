bool isIdentical(std::string str) {
	for(int i = 1; i < str.length(); i++) {
		if (str[i-1] != str[i]) {
			return false;
		}
	}
	return true;
}
