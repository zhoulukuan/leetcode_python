class UnionFind:
    def __init__(self):
        self.father = dict()
        self.weight = dict()

    def find(self, x):
        root = x
        base = 1
        while self.father[root] != None:
            base *= self.weight[root]
            root = self.father[root]

        while x != root:
            origin_father = self.father[x]
            self.father[x] = root
            self.weight[x], base = base, base / self.weight[x]
            x = origin_father
        return root

    def merge(self, x, y, xy_val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.weight[root_x] = self.weight[y] / self.weight[x] * xy_val

    def is_connected(self, x, y):
        return x in self.father and y in self.father and self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.weight[x] = 1

class Solution:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()
        for (x, y), val in zip(equations, values):
            uf.add(x)
            uf.add(y)
            uf.merge(x, y, val)

        res = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.weight[a] / uf.weight[b]
        return res
