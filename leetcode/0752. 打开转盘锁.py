from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends: return -1
        queue = deque()
        visited = set()
        queue.append('0000')
        visited.add('0000')
        for s in deadends: visited.add(s)
        surrounds = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0],
                [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1], [0, 0, 0, -1],]
        
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                num = queue.popleft()
                if num == target: return level
                for surround in surrounds:
                    next_num = self.compute(num, surround)
                    if next_num not in visited:
                        queue.append(next_num)
                        visited.add(next_num)
            level += 1
        return -1

    def compute(self, num, surround):
        s = ''
        for i in range(4):
            n = int(num[i]) + surround[i]
            if n == -1: n = 9
            elif n == 10: n = 1
            s += str(n)
        return s
