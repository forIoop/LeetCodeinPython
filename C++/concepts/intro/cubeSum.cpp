#include <cmath>
int sumOfCubes(std::vector<int> nums) {
	int total = 0;
	for(int i = 0; i < nums.size(); i++) {
		total += pow (nums[i],3);
	}
	return total;
}
