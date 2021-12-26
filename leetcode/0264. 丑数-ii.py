import heapq
class Solution:
    # 方法1: 三指针
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1, n):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if nums[i] == nums[i2] * 2: 
                i2 += 1
            if nums[i] == nums[i3] * 3: # 不能使用else if,因为会存在3*2和2*3为一个数的情况
                i3 += 1
            if nums[i] == nums[i5] * 5: 
                i5 += 1
        return nums[n - 1]

    # 方法2: 小顶堆
    def nthUglyNumber2(self, n: int) -> int:
        ans = []
        s = set()
        s.add(1)
        heapq.heappush(ans, 1)

        for _ in range(n):
            mini = heapq.heappop(ans)
            for num in (2, 3, 5):
                if mini * num not in s:
                    heapq.heappush(ans, mini * num)
                    s.add(mini * num)
        return mini
