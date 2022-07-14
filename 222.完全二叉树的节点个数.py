#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            res += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
"""
Accepted
18/18 cases passed (76 ms)
Your runtime beats 78.65 % of python3 submissions
Your memory usage beats 40.47 % of python3 submissions (22.1 MB)
"""
# @lc code=end

