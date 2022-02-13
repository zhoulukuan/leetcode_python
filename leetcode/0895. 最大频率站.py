from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.max_freq = 0
        self.counter = defaultdict(list)
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        f = self.freq[val]
        f += 1
        self.freq[val] = f
        self.counter[f].append(val)
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

    def pop(self) -> int:
        num = self.counter[self.max_freq].pop()
        self.freq[num] -= 1
        while not self.counter[self.max_freq] and self.max_freq > 0:
            self.max_freq -= 1
        return num
