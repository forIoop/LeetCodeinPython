bool double_letters(std::string word) {
	
	if(word.length() == 3) {
		if (word[1] == word[2]) {
			return true;
		}
	}
	
	
	for(int i = 0; i < word.length()-2; i++) {
		if(word[i] == word[i+1]) {
			return true;
		}
	}
	return false;
}
