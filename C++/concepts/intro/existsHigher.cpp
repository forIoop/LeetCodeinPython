bool existsHigher(std::vector<int> arr, int n) {
	for(int i = 0; i < arr.size(); i++) {
		if(arr[i] >= n) {
			return true;
		}
	}
	return false;
	
}
