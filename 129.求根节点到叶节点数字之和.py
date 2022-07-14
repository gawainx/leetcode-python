#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        # 对每个元祖，第一位为当前node，第二位储存root到当前node的和
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if node.left is None and node.right is None:
                res += val
                continue
            if node.left:
                stack.append((node.left, val * 10 + node.left.val))
            if node.right:
                stack.append((node.right, val * 10 + node.right.val))
        return res
"""
Accepted
108/108 cases passed (32 ms)
Your runtime beats 90.76 % of python3 submissions
Your memory usage beats 94.39 % of python3 submissions (14.8 MB)
"""
# @lc code=end

