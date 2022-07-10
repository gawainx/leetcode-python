#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        res = True
        idx_ = -1
        for idx, num in enumerate(nums):
            if num != mx:
                if mx - num < num:
                    res = False
            else:
                idx_ = idx
        return idx_ if res else -1
# @lc code=end

