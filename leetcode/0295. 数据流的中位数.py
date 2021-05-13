import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []


    def addNum(self, num: int) -> None:
        n1 = len(self.maxHeap)
        n2 = len(self.minHeap)
        n = n1 + n2
        if n == 0:
            self.minHeap.append(num)
            return
        if n == 1:
            num2 = self.minHeap[0]
            self.minHeap = [max(num, num2)]
            self.maxHeap = [-min(num, num2)]
            return

        v1 = -self.maxHeap[0]
        v2 = self.minHeap[0]
        if n1 == n2:
            if num <= v1: heapq.heappush(self.maxHeap, -num)
            else: heapq.heappush(self.minHeap, num)
        elif n1 > n2:
            if num >= v1: heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, -self.maxHeap[0])
                heapq.heappushpop(self.maxHeap, -num)
        else:
            if num <= v2: heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -self.minHeap[0])
                heapq.heappushpop(self.minHeap, num)

    def findMedian(self) -> float:
        n1 = len(self.maxHeap)
        n2 = len(self.minHeap)
        if n1 > n2:
            return -self.maxHeap[0]
        elif n1 < n2:
            return self.minHeap[0]
        else:
            return float(-self.maxHeap[0] + self.minHeap[0]) / 2
