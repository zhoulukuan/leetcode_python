class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] % n == 0:
                nums[i] = 1001

        # 用ID记录不用的环
        ID = 2000
        for i in range(n):
            if nums[i] > 1000: 
                continue
            
            index = i
            if nums[i] > 0:
                while 0 < nums[index] < 1000:
                    nums[index], index = ID, (index + nums[index]) % n
            else:
                while -1000 < nums[index] < 0:
                    nums[index], index = ID, (index + nums[index]) % n

            if nums[index] == ID:
                return True
            ID += 1
        return False
