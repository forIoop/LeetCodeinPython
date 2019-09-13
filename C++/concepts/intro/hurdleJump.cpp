bool hurdleJump(std::vector<int> hurdles, int jumpHeight) {
	for(int i = 0; i < hurdles.size(); i++) {
		if (hurdles[i] > jumpHeight) {
			return false;
		}
	}
	return true;
}
