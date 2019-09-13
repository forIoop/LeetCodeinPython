bool isPlural(std::string word) {
if(word.back() == 's' || word.back() == 'S')
	{
		return true;
	}
	else{
		return false;
	}
}
