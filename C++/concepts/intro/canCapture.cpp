bool canCapture(std::vector<std::string> pieces) {
	if (pieces[0][0] == pieces[1][0] || pieces[0][1] == pieces[1][1]) {
		return true;
	}
	return false;
}
