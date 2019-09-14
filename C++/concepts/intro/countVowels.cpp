int countVowels(std::string str) {
	int x=0;
	for(int i=0; i<str.size(); ++i){
		if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' ||
			str[i]=='A' ||str[i]=='E' ||str[i]=='I' ||str[i]=='O' ||str[i]=='U'){
			++x;
		}
	}
	return x;
}
