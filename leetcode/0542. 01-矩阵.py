from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[-1 for _ in range(n)] for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0
        curr_level = 1
        while q:
            curr_num = len(q)
            for _ in range(curr_num):
                x, y = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and ans[new_x][new_y] == -1:
                        ans[new_x][new_y] = curr_level
                        q.append((new_x, new_y))
            curr_level += 1
        return ans
