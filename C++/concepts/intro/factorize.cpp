std::vector<int> factorize(int n) {
	std::vector<int> arr = {};
	for(int i = 0; i < n; i++) {
		if(n % i == 0) {
			arr.push_back(i);
		}
	}
	return arr;
	
}
