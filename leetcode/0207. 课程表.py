from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegrees[course] += 1
            adjacency[pre].append(course)

        queue = deque()
        for i in range(numCourses):
            if not indegrees[i]: queue.append(i)

        while queue:
            course = queue.popleft()
            numCourses -= 1
            for n in adjacency[course]:
                indegrees[n] -= 1
                if not indegrees[n]: queue.append(n)
        return not numCourses
