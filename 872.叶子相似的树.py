#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_last(self, root1: Optional[TreeNode]):
        res = []
        stack = [root1]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                res.append(node.val)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = self.get_last(root1)
        l2 = self.get_last(root2)
        if len(l1) != len(l2):
            return False
        else:
            for n1, n2 in zip(l1, l2):
                if n1 != n2:
                    return False
            return True
# @lc code=end

