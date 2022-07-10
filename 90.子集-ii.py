#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# Note: 按照搜索树的每一层来展开；回溯的经典题目；在进行树展开之前排序然后保证子集后面元素不小于前面的元素可以去重
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        tree = [[[]]]

        for num in nums:
            tmp = []
            last_layer = tree[-1]
            for node in last_layer:
                tmp.append(node)
                tmp.append(node + [num])
            tree.append(tmp)
        res = []
        for item in tree[-1]:
            item.sort()
            if item not in res:
                res.append(item)
        return res
# @lc code=end

