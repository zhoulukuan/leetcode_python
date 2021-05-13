import collections
import heapq
class Solution:
    def reorganizeString(self, s):
        times = collections.Counter(s)
        heap = []
        for c, t in times.items():
            heapq.heappush(heap, (-t, c))

        ans = "#"
        for _ in range(len(s)):
            item = heapq.heappop(heap)
            t, c = -item[0], item[1]
            if c != ans[-1]:
                ans += c
                if t - 1 > 0:
                    heapq.heappush(heap, (1 - t, c))
            else:
                if len(heap) == 0: return ""
                item = heapq.heappop(heap)
                tt, cc = -item[0], item[1]
                ans += cc
                if tt - 1 > 0:
                    heapq.heappush(heap, (1 - tt, cc))
                heapq.heappush(heap, (-t, c))
        return ans[1:]
