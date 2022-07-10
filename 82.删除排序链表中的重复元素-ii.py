#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        prev, curr = dummy_head, head
        nums = set()
        rep_nums = set()
        while curr:
            if curr.val in nums:
                rep_nums.add(curr.val)
                prev.next = curr.next
                curr.next = None
                curr = prev.next
                continue
            else:
                nums.add(curr.val)
                prev = curr
                curr = curr.next
        prev, curr = dummy_head, head
        while curr:
            if curr.val in rep_nums:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
                continue
            else:
                prev = curr
                curr = curr.next
        return dummy_head.next
# @lc code=end

