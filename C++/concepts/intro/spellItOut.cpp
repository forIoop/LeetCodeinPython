std::vector<std::string> spelling(std::string str) {
	std::vector<std::string> output = {};
	std::string result = "";
	for(int i = 0; i < str.length(); i++) {
		result += str[i];
		output.push_back(result);
	}
	return output;
}
