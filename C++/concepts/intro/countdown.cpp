std::vector<int> countdown(int start) {
	std::vector<int> arr = {};
	for(int i = start; i >= 0; i--) {
		arr.push_back(i);
	}
	return arr;
}
