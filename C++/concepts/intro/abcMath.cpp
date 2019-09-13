bool abcmath(int a, int b, int c){
	for (int i = 0; i  < b; i++) {
		a+=a;
	}	
	return a%c == 0;
}
