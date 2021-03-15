class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        num1 = (n + m - 1) // 2 + 1
        num2 = (n + m) // 2 + 1
        if num1 == num2:
            return self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, num1)
        else:
            return self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, num1) * 0.5 + self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, num2) * 0.5

    # 辅助函数: 从序列中选择第num小的数
    def getKth(self, nums1, start1, end1, nums2, start2, end2, num):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            # 保持nums1的长度是中小于nums2,避免多分支的情况
            return self.getKth(nums2, start2, end2, nums1, start1, end1, num)
        if len1 == 0:
            # nums1已经没有元素,直接从nums2中选择
            return nums2[start2 + num - 1]

        # k=1的时候,无法再对半减少,直接返回两个数列最小的那个
        if num == 1:
            return min(nums1[start1], nums2[start2])

        # 每次对半选择
        # 从nums1和nums2中各取前k元素,因为共有2k<=num个元素,看哪边小就丢掉哪边
        # 所以2k中最大的元素会被保留下来,而num则会减少k个元素
        # 举例nums1=[1,4,6],nums2=[2,5,7,10],num=6,k=3
        # nums1中选择了1,4,6,nums2中选择了2,5,7,由于6<7,所以把nums1中的3个都丢掉,这里第6小的元素也就是7一定不会丢掉
        k = num // 2
        if len1 >= k:
            p1, n1 = start1 + k - 1, nums1[start1 + k - 1]
            p2, n2 = start2 + k - 1, nums2[start2 + k - 1]
        else:
            # 若nums1长度小于k的特殊情况
            p1, n1 = end1, nums1[end1]
            p2, n2 = start2 + num - len1 - 1, nums2[start2 + num - len1 - 1]


        if n1 <= n2:
            return self.getKth(nums1, p1 + 1, end1, nums2, start2, end2, num - (p1 - start1 + 1))
        else:
            return self.getKth(nums1, start1, end1, nums2, p2 + 1, end2, num - (p2 - start2 + 1))
