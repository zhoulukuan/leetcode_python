from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 每门课程依赖的前置课程数 
        rely = [0 for _ in range(numCourses)]
        # 每门课程后置可开启的课程数
        next_courses = [[] for _ in range(numCourses)]

        for j, i in prerequisites:
            rely[j] += 1
            next_courses[i].append(j)

        q = deque()
        for i in range(numCourses):
            # 前置课程为0的入列
            if rely[i] == 0:
                q.append(i)
        
        while q:
            # 前置课程数为零的课程出列
            # 课程数-1
            # 该课程学习后可开启的那些课程的依赖数也-1,若为0则说明可以入列学习了
            curr = q.popleft()
            numCourses -= 1
            for next_course in next_courses[curr]:
                rely[next_course] -= 1
                if rely[next_course] == 0:
                    q.append(next_course)
        return numCourses == 0
