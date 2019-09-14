bool isStrangePair(std::string str1, std::string str2) {
	if(str1[0] == str2[str2.length()-1]) {
		return true;
	}
	return false;
}
