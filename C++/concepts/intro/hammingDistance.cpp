int hammingDistance(std::string str1, std::string str2) {
	int distance = 0;
	for(int i = 0; i < str1.length(); i++) {
		if (str1[i] != str2[i]) {
			distance += 1;
		}
	}
	return distance;
}
