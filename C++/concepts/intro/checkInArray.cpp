bool check(std::vector<int> arr, int el) {
	for(int i = 0; i < arr.size(); i++) {
		if(arr[i] == el) {
				return true;
		}
	}
	return false;
}
