#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)
        fast, slow = dummy_head, dummy_head
        for _ in range(n + 1):
            fast = fast.next
            if fast is None:
                break
        while fast:
            fast = fast.next
            slow = slow.next
        if slow.next:
            tmp = slow.next
            slow.next = tmp.next
            tmp.next = None
        return dummy_head.next
# @lc code=end

