from collections import deque
class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        n = len(routes)
        routes = [set(route) for route in routes]
        visited_routes = set()
        visited_station = set()
        queue = deque()
        queue.append(source)

        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                station = queue.popleft()
                if station == target: return level
                for i in range(n):
                    route = routes[i]
                    if i not in visited_routes and station in route:
                        for s in route:
                            queue.append(s)
                            if s not in visited_station: visited_station.add(s)
                        visited_routes.add(i)
            level += 1
        return -1
