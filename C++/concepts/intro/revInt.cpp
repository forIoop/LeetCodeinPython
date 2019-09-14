std::string rev(int n) {
std::string nString =	std::to_string(n);
std::string revString = "";
	for(int i = nString.length()-1; i >= 0; i--) {
		if(nString[i] != '-'){
			revString += nString[i];
		}
	}
	return revString;
}
