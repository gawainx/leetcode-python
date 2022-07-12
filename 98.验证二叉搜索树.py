#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    visit_nums = []
    
    def visits(self, root: TreeNode):
        if root is None:
            return []
        res = []
        if root.left:
            res.extend(self.visits(root.left))
        res.append(root.val)
        if root.right:
            res.extend(self.visits(root.right))
        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vis = self.visits(root)
        result = True
        if len(vis) == 1:
            return True
        prev = vis[0]
        for num in vis[1:]:
            if num <= prev:
                return False
            prev = num
        return True
"""
Accepted
80/80 cases passed (72 ms)
Your runtime beats 7.4 % of python3 submissions
Your memory usage beats 32.85 % of python3 submissions (18 MB)
"""
# @lc code=end

