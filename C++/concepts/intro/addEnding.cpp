std::vector<std::string> addEnding(std::vector<std::string> arr, std::string ending) {
	for(int i = 0; i < arr.size(); i++) {
		arr[i] += ending;
	}
	return arr;
}
