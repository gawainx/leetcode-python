#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        num_odds = 0
        num_ones = 0
        res = 0
        if len(cnt) == 1:
            return len(s)
        for k, v in cnt.items():
            if v % 2 == 0:
                res += v
            else:
                num_odds += 1
                if v != 1:
                    res += (v - 1)
                    num_odds += 1
                else:
                    num_ones += 1
        if num_ones != 0 or num_odds != 0:
            res += 1
        return res
# @lc code=end

