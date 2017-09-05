#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name : Find_the_Closest_Palindrome.py
# Author: Ding Weiqin
# Mail : D_VIKING@163.COM
# Created Time: 9/5/17 2:15 PM

__author__ = 'Ding Weiqin'


# 时间超限。。。
class Solution(object):

    def is_palindrome(self, n):
        n = self.intSp2List(n)
        while len(n) > 1:
            a = n.pop(0)
            b = n.pop(len(n) - 1)
            if a != b:
                return False
        return True

    def intSp2List(self, n):
        l = []
        while n >= 1:
            l.insert(0, int(n % 10))
            n = int(n / 10)
        return l


    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        #a往小方向找，b往大方向找
        a = int(n) - 1
        b = int(n) + 1
        n = int(n)


        while not self.is_palindrome(a) and not self.is_palindrome(b):
            a -= 1
            b += 1

        if self.is_palindrome(a) and not self.is_palindrome(b):
            return str(a)
        if self.is_palindrome(b) and not self.is_palindrome(a):
            return str(b)

        if abs(a - n) <= abs(b - n):
            return str(a)
        else:
            return str(b)


if __name__ == '__main__':
    n = "666666666"
    s = Solution()
    print(s.nearestPalindromic(n))

