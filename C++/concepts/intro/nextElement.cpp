int nextElement(std::vector<int> arr) {
	int difference = arr[1] - arr[0];
	return arr[arr.size()-1] + difference;
}
