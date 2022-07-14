#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        ln1, ln2 = len(nums1), len(nums2)
        while True:
            if i >= ln1 or j >= ln2:
                break
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # nums1[i] == nums2[j]
                while nums1[i] == nums2[j]:
                    # 需要判断是否飞了
                    res.append(nums1[i])
                    i += 1
                    j += 1
                    if i >= ln1 or j >= ln2:
                        break
        return res
# @lc code=end

