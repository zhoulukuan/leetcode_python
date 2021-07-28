class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        ans = []

        trie = {}
        for word in words:
            p = trie
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['finish'] = word

        def dfs(x, y, p):
            c = board[x][y]

            if 'finish' in p[c]:
                ans.append(p[c]['finish'])
                p[c].pop('finish')

            board[x][y] = '#'
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] in p[c]:
                    dfs(new_x, new_y, p[c])
            board[x][y] = c

            if not p[c]:
                p.pop(c)


        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return ans
