std::vector<int> transform(std::vector<int> arr) {
	for(int i = 0; i < arr.size(); i++) {
		if (arr[i] % 2 == 1) {
			arr[i] += 1;
		}
		else {
			arr[i] -= 1;
		}
	}
	return arr;
}
