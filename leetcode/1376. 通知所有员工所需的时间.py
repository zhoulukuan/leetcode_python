class UnionFind:
    def __init__(self):
        self.father = {}
        self.weight = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.weight[x] = 0

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.weight[root_x] = self.weight[y] - self.weight[x] + val

    def find(self, x):
        root = x
        base = 0

        while self.father[root] != None:
            base += self.weight[root]
            root = self.father[root]

        while x != root:
            origin_father = self.father[x]
            self.weight[x], base = base, base - self.weight[x]
            self.father[x] = root
            x = origin_father
        return root

    def flat(self):
        for i in self.father.keys():
            self.find(i)


class Solution:
    def numOfMinutes(self, n: int, headID, manager, informTime) -> int:
        uf = UnionFind()
        for i in range(n):
            uf.add(i)
            if i != headID:
                uf.add(manager[i])
                uf.merge(i, manager[i], informTime[manager[i]])
        uf.flat()
        return max(uf.weight.values())
