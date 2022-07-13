# @before-stub-for-debug-begin
from python3problem1046 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#
from typing import List
# @lc code=start

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ln = len(stones)
        while ln > 1:
            stones.sort(reverse=True)
            max_st, sub_max_st = stones[0], stones[1]
            stones = stones[2:]
            ln -= 2
            if max_st != sub_max_st:
                sub = max_st - sub_max_st
                stones.append(sub)
                ln += 1
        if ln == 1:
            return stones[0]
        else:
            return 0


# @lc code=end

