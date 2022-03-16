from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set()
        for end in deadends:
            dead.add(end)
        if '0000' in dead: return -1

        q = deque()
        q.append('0000')
        visit = set()
        visit.add('0000')
        curr_level = 0
        while q:
            curr_num = len(q)
            for _ in range(curr_num):
                nums = q.popleft()
                if nums == target:
                    return curr_level
                for i in range(4):
                    c1 = int(nums[i]) - 1
                    c2 = int(nums[i]) + 1
                    if c1 == -1: c1 = 9
                    if c2 == 10: c2 = 0
                    for j in (c1, c2):
                        new_num = list(nums)
                        new_num[i] = str(j)
                        new_num = "".join(new_num)
                        if new_num not in visit and new_num not in dead:
                            visit.add(new_num)
                            q.append(new_num)
            curr_level += 1
        return -1
