#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        src = list(s)
        i = 0
        j = len(src) - 1
        while i < j:
            if src[i].isalpha() and src[j].isalpha():
                src[i], src[j] = src[j], src[i]
                i += 1
                j -= 1
                continue
            else:
                if not src[i].isalpha():
                    i += 1
                if not src[j].isalpha():
                    j -= 1
                continue
        return ''.join(src)
"""
Accepted
115/115 cases passed (32 ms)
Your runtime beats 88.63 % of python3 submissions
Your memory usage beats 94.67 % of python3 submissions (14.8 MB)
"""
# if __name__ == '__main__':
#     slv = Solution()
#     print(slv.reverseOnlyLetters("ab-cd"))
# @lc code=end

