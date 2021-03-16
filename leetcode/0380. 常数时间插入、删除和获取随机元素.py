import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos: return False
        self.data.append(val)
        self.pos[val] = len(self.data) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos: return False
        p1 = self.pos[val]
        p2 = len(self.data) - 1
        if p1 != p2:
            self.pos.pop(val)
            self.data[p1] = self.data[p2]
            self.data.pop()
            self.pos[self.data[p1]] = p1
        else:
            self.data.pop()
            self.pos.pop(val)
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        n = random.randint(0, len(self.data) - 1)
        return self.data[n]
