# @before-stub-for-debug-begin
from python3problem143 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        table = []
        node = head
        while node:
            table.append(node)
            node = node.next
        i, j = 0, len(table) - 1
        while i < j:
            table[i].next = table[j]
            i += 1
            if i == j :
                break
            table[j].next = table[i]
            j -= 1
        # set final node
        table[i].next = None
# @lc code=end

