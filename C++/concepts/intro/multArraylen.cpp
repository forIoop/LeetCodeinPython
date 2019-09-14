std::vector<int> multiplyByLength(std::vector<int> arr) {
	for(int i = 0; i < arr.size(); i++) {
		arr[i] = arr[i] * arr.size();
	}
	return arr;
}
