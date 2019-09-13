using namespace std;
string cppStr(vector <char> cStr){
	string result = "";
	for(int i = 0; i < cStr.size()-1; i++) {
		result += cStr[i];
	}
	return result;
}
