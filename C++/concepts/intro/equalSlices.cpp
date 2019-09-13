bool equalSlices(int total, int people, int each) {
	if (people * each <= total) {
		return true;
	}
	return false;
}
