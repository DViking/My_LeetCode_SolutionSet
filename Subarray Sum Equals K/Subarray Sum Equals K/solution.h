#pragma once
#include <vector>
using namespace std;

class solution
{
public:
	solution();
	~solution();
	int subarraySum(vector<int>& nums, int k);
	int k;
	vector<int> nums;
};

