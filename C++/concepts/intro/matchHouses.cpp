int matchHouses(int step) {
	if(step == 0) {
		return 0;
	}
	if(step == 1) {
		return 6;
	}
	
	else {
		return 5 + matchHouses(step - 1);
	}
}
