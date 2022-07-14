#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        all_results = []
        wait_for_build = [[root]]
        while len(wait_for_build) != 0:
            latest_path = wait_for_build.pop()
            last_node = latest_path[-1]
            if last_node.left is None and last_node.right is None:
                all_results.append('->'.join([str(node.val) for node in latest_path]))
            if last_node.left:
                new_path = latest_path[:]
                new_path.append(last_node.left)
                wait_for_build.append(new_path)
            if last_node.right:
                new_path = latest_path[:]
                new_path.append(last_node.right)
                wait_for_build.append(new_path)
        return all_results
        
# @lc code=end

