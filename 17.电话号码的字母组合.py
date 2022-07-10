# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ln = len(digits)
        keyboard = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3':'def',
            '4': 'ghi',
            '5': 'jkl', 
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        stk = []
        # initialize stack
        if len(digits) == 0:
            return []
        for chr in keyboard[digits[0]]:
            stk.append([(chr, 0)])
        while len(stk) != 0:
            last_path = stk.pop()
            if len(last_path) == ln:
                r_= ''
                for chr, _ in last_path:
                    r_ += chr
                res.append(r_)
                continue
            last_idx = last_path[-1][1]
            if last_idx < ln - 1:
                for chr in keyboard[digits[last_idx + 1]]:
                    stk.append(last_path + [(chr, last_idx + 1)])
        return res
# @lc code=end

