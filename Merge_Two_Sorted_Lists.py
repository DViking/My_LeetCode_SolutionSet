#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name : Merge_Two_Sorted_Lists.py
# Author: Ding Weiqin
# Mail : D_VIKING@163.COM
# Created Time: 9/5/17 3:56 PM

__author__ = 'Ding Weiqin'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2

        result = ListNode()
        pr = result
        while p1.next != None or p2.next != None:
            if p1.val <= p2.val:
                p = ListNode(p1.val)
                p1 = p1.next

            else:
                p = ListNode(p2.val)
                p2 = p2.next
            pr.next = p
            pr = p

        if p1.next == None:
            pr.next = p2
        elif p2.next == None:
            pr.next = p1



        return result