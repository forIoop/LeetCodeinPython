int calc_determinant(std::vector<std::vector<int>> arr) {
	return (arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0]);
}
