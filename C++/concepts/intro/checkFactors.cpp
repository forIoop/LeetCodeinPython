bool checkFactors(std::vector<int> factors, int num) {
	for(int i = 0; i < factors.size(); i++) {
		if(num % factors[i] != 0) {
			return false;
		}
	}
	return true;
}
