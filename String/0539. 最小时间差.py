class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) <= 1: return 0
        self.max = 24 * 60
        timePoints.sort()
        n = len(timePoints)
        ans = self.max
        for i in range(n - 1):
            left = timePoints[i]
            right = timePoints[i + 1]
            ans = min(self.diff(left, right), ans)
        ans = min(ans, self.diff(timePoints[0], timePoints[-1]))
        return ans

    def diff(self, t1, t2):
        t1 = t1.split(':')
        t2 = t2.split(':')
        if t1[0] == t2[0]:
            return abs(int(t1[1]) - int(t2[1]))
        else:
            t1 = int(t1[0]) * 60 + int(t1[1])
            t2 = int(t2[0]) * 60 + int(t2[1])
            return min(abs(t2 - t1), self.max - abs(t2 - t1))
