int word(std::string str) {
	std::vector<std::string> arr={"zero","one","two","three","four","five",
																"six","seven","eight","nine"};
	for(int i = 0; i < arr.size(); i++) {
		if (arr[i] == str) {
			return i;
		}
	}
	return 0;
}
	
