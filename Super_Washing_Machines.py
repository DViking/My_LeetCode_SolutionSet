#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name : Super_Washing_Machines.py
# Author: Ding Weiqin
# Mail : D_VIKING@163.COM
# Created Time: 9/5/17 11:26 AM

__author__ = 'Ding Weiqin'


class Solution(object):
    def __init__(self):
        self.all = 0
        self.average = 0
        self.answer = 0

    def findMinMoves(self, machines):

        """
        :type machines: List[int]
        :rtype: int
        """
        self.all = sum(machines)
        if (self.all % len(machines)) != 0:
            return -1
        self.average = int(self.all/len(machines))
        #将序列改为正负关系序列
        move = []
        for i in range(len(machines)):
            move.append(machines[i] - self.average)

        self.answer = 0
        mm = 0

        for i in range(len(move)):
            self.answer += move[i]
            mm = max(abs(self.answer), mm)


        return max(mm, max(move))



if __name__ == '__main__':

    a = Solution()
    l = [0, 3, 0]
    print(a.findMinMoves(l))

