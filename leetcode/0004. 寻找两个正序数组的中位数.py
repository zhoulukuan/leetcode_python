class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        if (m + n) % 2 == 1:
            k = (m + n + 1) // 2
            index1, index2 = self.helper(nums1, nums2, k - 1, 0, 0)
            # 数组元素个数是奇数,剔除k-1个数后直接返回较小值
            if index1 == n:
                return nums2[index2]
            elif index2 == m:
                return nums1[index1]
            else:
                return min(nums1[index1], nums2[index2])
        else:
            k = (m + n) // 2
            index1, index2 = self.helper(nums1, nums2, k - 1, 0, 0)
            # 数组个数是偶数,要从index1和index2出发得到两个最小的值
            if index1 == n:
                v1, v2 = nums2[index2], nums2[index2 + 1]
            elif index2 == m:
                v1, v2 = nums1[index1], nums1[index1 + 1]
            else:
                if nums1[index1] <= nums2[index2]:
                    v1 = nums1[index1]
                    index1 += 1
                else:
                    v1 = nums2[index2]
                    index2 += 1
                if index1 == n:
                    v2 = nums2[index2]
                elif index2 == m:
                    v2 = nums1[index1]
                else:
                    v2 = min(nums1[index1], nums2[index2])
            return float(v1 + v2) / 2

    # 辅助函数,从数组中剔除前k个最小的数后指针所在位置
    def helper(self, nums1, nums2, k, index1, index2):
        # 考察某个数组已经剔除完的情况
        if index1 == len(nums1):
            return index1, index2 + k
        if index2 == len(nums2):
            return index1 + k, index2

        # 递归终止点
        # k=0,直接返回;k=1,剔除开头最小元素后返回
        if k == 1:
            return (index1 + 1, index2) if nums1[index1] <= nums2[index2] else (index1, index2 + 1)
        if k == 0:
            return index1, index2

        # 每次剔除k//2个元素
        n = k // 2
            # 数组长度可能不够n,计算每个数组能剔除的最多的数
        n1 = min(n, len(nums1) - index1)
        n2 = min(n, len(nums2) - index2)
        if nums1[index1 + n1 - 1] <= nums2[index2 + n2 - 1]:
            k -= n1
            p1, p2 = self.helper(nums1, nums2, k, index1 + n1, index2)
        else:
            k -= n2
            p1, p2 = self.helper(nums1, nums2, k, index1, index2 + n2)
        return p1, p2
