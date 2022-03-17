from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        routes = [set(route) for route in routes]
        n = len(routes)
        visisted = [False for _ in range(n)]


        q = deque()
        for i, route in enumerate(routes):
            if source in route:
                q.append(route)
                visisted[i] = True
        curr_level = 1

        while q:
            curr_num = len(q)
            for _ in range(curr_num):
                curr_route = q.popleft()
                if target in curr_route:
                    return curr_level
                for station in curr_route:
                    for i, next_route in enumerate(routes):
                        if not visisted[i] and station in next_route:
                            visisted[i] = True
                            q.append(next_route)
            curr_level += 1
        return -1
