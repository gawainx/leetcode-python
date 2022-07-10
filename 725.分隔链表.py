#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
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
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        ln = 0
        node = head
        # calculate length of linked list
        while node:
            ln += 1
            node = node.next
        res = []
        if ln > k:
            parts = ln // k
            others = ln % k
            counts = [parts for _ in range(k)]
            for i in range(others):
                counts[i] += 1
            start = ListNode(next=head)
            for i in range(k):
                ln_ = 0
                prev = start
                curr = start.next
                while ln_ < counts[i] and curr:
                    ln_ += 1
                    prev = curr
                    curr = curr.next
                prev.next = None
                res.append(start.next)
                start = ListNode(next=curr)
        elif ln == k:
            node = head
            while node:
                res.append(node)
                node = node.next
            for node in res:
                node.next = None
        else:
            # ln < k
            node = head
            while node:
                res.append(node)
                node = node.next
            for node in res:
                node.next = None
            while len(res) < k:
                res.append(None)
        return res
# @lc code=end

