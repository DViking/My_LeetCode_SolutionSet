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

    def group(self, move):
        pass


    def change(self, group):
        pass

    def isOkay(self, move):
        for i in move:
            if move[i] != 0:
                return False
        return True

    def findMinMoves(self, machines):

        """
        :type machines: List[int]
        :rtype: int
        """
        self.all = sum(machines)

        if (self.all % len(machines)) != 0:
            return -1

        self.average = int(self.all/len(machines))

        # print(self.average)
        # print(len(machines))

        move = []


        for i in range(len(machines)):
            move.append(self.average - machines[i])

        self.answer = 0

        #相邻可以每次移动一件，而不是一次只能移动一件（应该用动态规划解决）

        while not isOkay(move):
            group(move)
            change(move)
            self.answer += 1

        return self.answer

        # for i in range(len(move)):
        #     if move[i] > 0:
        #         self.answer += move[i]
        #
        # return self.answer



if __name__ == '__main__':

    a = Solution()
    l = [4, 0, 0, 4]
    print(a.findMinMoves(l))

