#include "solution.h"


solution::solution()
{
	k = 0;

}


solution::~solution()
{
}

int solution::subarraySum(vector<int>& nums, int k){
	int count = 0;
	int subarrayNums = 0;
	for (int i = 0; i < nums.size(); i++)
	{
		for (int j = i; j < nums.size(); j++)
		{
			count += nums[j];
			if (count == k) {
				subarrayNums++;
			}
		}
		count = 0;
	}
	return subarrayNums;
}
