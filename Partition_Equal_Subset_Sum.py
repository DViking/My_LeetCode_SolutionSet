#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name : Partition_Equal_Subset_Sum.py
# Author: Ding Weiqin
# Mail : D_VIKING@163.COM
# Created Time: 9/5/17 4:35 PM

__author__ = 'Ding Weiqin'


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums, reverse=True)
        print(nums)

        count = sum(nums)
        if count % 2 != 0:
            return False

        ave = - (count / 2)

        #list 用于记录已经加如计算的数，用于回溯
        list=[]

        for i in range(len(nums)):
            ave += nums[i]
            list.append(i)
            if ave == 0:
                return True

            #超过平均值，产生回溯

            if ave > 0:
                i = list.pop()
                ave -= nums[i]

            #加到最后一项仍然小于目标值，产生回溯
            if i == len(nums) - 1:
                i = list.pop()
                ave -= nums[i]

        return False



if __name__ == '__main__':
    l = [71,70,66,54,32,63,38,98,4,22,61,40,6,8,6,21,71,36,30,34,44,60,89,53,60,56,73,14,63,37,15,58,51,88,88,32,80,32,10,89,67,29,68,65,34,15,88,8,57,78,37,63,73,65,47,39,32,74,31,44,43,4,10,8,96,22,58,87,29,99,79,13,96,21,62,71,34,55,72,3,96,7,36,64,30,6,14,87,12,90,40,13,29,21,94,33,99,86,4,100]
    s = Solution()
    print(s.canPartition(l))



