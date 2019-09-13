bool profitableGamble(float prob, int prize, float pay) {
	if (prob * prize > pay) {
		return true;
	}
	return false;
}
