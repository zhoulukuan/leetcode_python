import random
import bisect
class Solution:
    def __init__(self, w: List[int]):
        s = sum(w)
        self.probability = [weight for weight in w]
        for i in range(len(w)):
            self.probability[i] /= float(s)
            if i > 0:
                self.probability[i] += self.probability[i - 1]
            

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.probability, random.random())
