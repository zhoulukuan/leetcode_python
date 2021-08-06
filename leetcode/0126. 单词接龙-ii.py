from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList: return []
        # bfs
        successor = {}
        self.find_successor(beginWord, endWord, wordList, successor)

        # dfs
        ans = []
        self.find_path(beginWord, endWord, successor, ans)

        return ans

    def differ(self, str1, str2):
        n = len(str1)
        count = 0
        for i in range(n):
            if str1[i] != str2[i]:
                count += 1
            if count > 1: return count
        return count

    def find_successor(self, beginWord, endWord, wordList, successor):
        n = len(wordList)

        queue = deque()
        queue.append(beginWord)
        successor[beginWord] = {'lvl': 0, 'from': []}
        level = 1
        find_end = False
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    find_end = True
                for i in range(n):
                    curr_word = wordList[i]
                    if (curr_word in successor and successor[curr_word]['lvl'] < level) or self.differ(word, curr_word) != 1: continue
                    if curr_word in successor:
                        successor[curr_word]['from'].append(word)
                    else:
                        queue.append(curr_word)
                        successor[curr_word] = {'lvl': level, 'from': [word]}
            if find_end: return level
            level += 1
        return level

    def find_path(self, beginWord, endWord, successor, ans):
        if endWord not in successor: return
        def backtracking(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for next_word in successor[word]['from']:
                path.append(next_word)
                backtracking(next_word, path)
                path.pop()
        backtracking(endWord, [endWord])
