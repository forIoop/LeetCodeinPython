std::vector<int> negate(std::vector<int> vi) {
	for(int i = 0; i < vi.size(); i++) {
		vi[i] *= -1;
	}
	return vi;
}
