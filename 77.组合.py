# @before-stub-for-debug-begin
from python3problem77 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            res = []
            for num in range(1, n + 1):
                res.append([num])
            return res
        all_nums = [i for i in range(1, n + 1)]
        results = []
        stk = []
        # initialize stack
        for num in all_nums:
            if num != n:
                stk.append([num])
        # search until stack is empty
        while len(stk) != 0:
            last_path = stk.pop()
            if len(last_path) == k:
                results.append(last_path)
                continue
            last_item = last_path[-1]
            for idx in range(last_item+1, n+1):
                lp_ = last_path[:]
                lp_.append(idx)
                stk.append(lp_)
        return results

# @lc code=end

