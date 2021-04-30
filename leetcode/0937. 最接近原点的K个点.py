class Solution:
    def kClosest(self, points, k: int):
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            point.append(distance)
        self.sort(points, 0, len(points) - 1, k)
        return [point[:2] for point in points[:k]]

    def sort(self, points, start, end, k):
        if start >= end: return
        boundary = start
        pivot = points[end][-1]
        for i in range(start, end):
            if points[i][-1] < pivot:
                points[boundary], points[i] = points[i], points[boundary]
                boundary += 1
        points[boundary], points[end] = points[end], points[boundary]
        self.sort(points, start, boundary - 1, k)
        self.sort(points, boundary + 1, end, k)
