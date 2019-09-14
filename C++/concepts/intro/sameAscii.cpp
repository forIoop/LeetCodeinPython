bool sameAscii(std::string a, std::string b) {
	int ascii_a = 0;
	int ascii_b = 0;
	for(int i = 0; i < a.length(); i++) {
		ascii_a += int(a[i]);
	}
	for(int i = 0; i < b.length(); i++) {
		ascii_b += int(b[i]);
	}
	if(ascii_a == ascii_b) {
		return true;
	}
	return false;
}
