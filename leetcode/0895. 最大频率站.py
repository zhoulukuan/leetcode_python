from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.stack = defaultdict(list)
        self.counter = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        f = self.counter[val] + 1
        self.counter[val] = f
        if f > self.maxFreq:
            self.maxFreq = f
        self.stack[f].append(val)

    def pop(self) -> int:
        res = self.stack[self.maxFreq].pop()
        self.counter[res] -= 1
        while not self.stack[self.maxFreq] and self.maxFreq > 0:
            self.maxFreq -= 1
        return res
