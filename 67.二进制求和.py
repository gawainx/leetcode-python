#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start

class Solution:
    mapper = {
        # x, y and carry -> cur, carry
        '000': ('0', '0'),
        '001': ('1', '0'),
        '010': ('1', '0'),
        '011': ('0', '1'),
        '100': ('1', '0'),
        '101': ('0', '1'),
        '110': ('0', '1'),
        '111': ('1', '1')
    }

    def addBinary(self, a: str, b: str) -> str:
        lna = len(a)
        lnb = len(b)
        # 判断长度，对齐
        if lna > lnb:
            b = '0' * (lna - lnb) + b
        else:
            a = '0' * (lnb - lna) + a
        carry_out = '0'
        res = []
        # 使用加法器方法计算每个bit的结果
        # 因为是从低到高运算，所以需要反转
        for x, y in zip(reversed(a), reversed(b)):
            cur, carry_out = self.mapper[x+y+carry_out]
            # res += cur
            res.append(cur)
        if carry_out != '0':
            res.append(carry_out)
        r = ''
        for c in reversed(res):
            r += c
        idx = 0
        # 去掉先导0
        while r[idx] == '0':
            idx += 1
            # 如果运算全0或者前面很多0，保留最后一位
            if idx >= len(r):
                return r[-1]
        return r[idx:]
# @lc code=end

