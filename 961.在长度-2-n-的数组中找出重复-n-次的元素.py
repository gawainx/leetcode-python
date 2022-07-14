#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#
from typing import List
# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for gap in range(1, 5):
            for idx in range(0, n - gap):
                if nums[idx] == nums[idx + gap]:
                    return nums[idx]
# @lc code=end

