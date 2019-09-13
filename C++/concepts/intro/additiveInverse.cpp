std::vector<int> additiveInverse(std::vector<int> arr) {
	for(int i = 0; i < arr.size(); i++) {
		arr[i] *= -1;
	}
	return arr;
	
}
