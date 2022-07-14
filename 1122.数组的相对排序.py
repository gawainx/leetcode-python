#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rest = []
        res = []
        arr2idx = {}
        cnt = Counter(arr1)
        for idx, num in enumerate(arr2):
            for _ in range(cnt[num]):
                res.append(num)
        for num in arr1:
            if num not in res:
                rest.append(num)
        rest.sort()
        return res + rest

# @lc code=end

