

#include "pch.h"
#include <map>
#include <iostream>
using namespace std;

int main()
{
	string s1 = "aabcccccaaa";
	string s2 = "abcd";
	map<char, int> hm;

	for (int i = 0; i < s1.length(); i++)
	{
		cout << s1.at(i);
		hm[i] = s1.at(i);
	}
	cout << endl;
	cout << char(hm.);
	

}
