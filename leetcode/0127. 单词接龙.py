from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n = len(wordList)
        visited = [False for _ in range(n)]

        queue = deque()
        queue.append(beginWord)
        level = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord: return level
                for i in range(n):
                    if not visited[i] and self.differ(word, wordList[i]) == 1:
                        queue.append(wordList[i])
                        visited[i] = True
            level += 1
        return 0

    def differ(self, str1, str2):
        n = len(str1)
        count = 0
        for i in range(n):
            if str1[i] != str2[i]:
                count += 1
            if count > 1: return count
        return count
