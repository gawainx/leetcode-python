# @before-stub-for-debug-begin
from python3problem216 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [_ for _ in range(1, 10)]
        results = []
        stack = [[num] for num in nums]
        while len(stack) != 0:
            path = stack.pop()
            if len(path) == k:
                if sum(path) == n:
                    results.append(path)
                continue
            last_num = path[-1]
            for n_ in range(last_num + 1, 10):
                    stack.append(path + [n_])
        return results
# @lc code=end

