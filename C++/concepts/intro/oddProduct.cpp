int oddProduct(std::vector<int> arr) {
	int product = 1;
	for(int i = 0; i < arr.size(); i++) {
		if(arr[i] % 2 == 1) {
			product *= arr[i];
		}
	}
	return product;
		
