#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        al = 'aeiouAEIOU'
        lt = []
        src = list(s)
        for idx, chr in enumerate(src):
            if chr in al:
                lt.append((idx, chr))
        i = 0
        j = len(lt) - 1
        while i < j:
            src[lt[i][0]] = lt[j][1]
            src[lt[j][0]] = lt[i][1]
            i += 1
            j -= 1
        return ''.join(src)
# @lc code=end

