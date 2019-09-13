using namespace std;
int findIndex(vector<string> arr, string str) {
	for(int i = 0; i < arr.size(); i++) {
		if(arr[i] == str) {
			return i;
		}
	}
	return -1;
}
