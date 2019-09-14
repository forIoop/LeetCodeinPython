std::vector<int> findEvenNums(int num) {
	std::vector<int> arr = {};
	for(int i = 1; i <= num; i++ ) {
		if(i % 2 == 0) {
			arr.push_back(i);
		}
	}
	return arr;
}
