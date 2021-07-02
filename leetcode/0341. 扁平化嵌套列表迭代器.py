class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        def dfs(nests):
            for nest in nests:
                if nest.isInteger():
                    self.queue.append(nest.getInteger())
                else:
                    dfs(nest.getList())
        dfs(nestedList)

    def next(self) -> int:
        if self.hasNext():
            return self.queue.pop(0)
        else:
            return -1
    
    def hasNext(self) -> bool:
        return len(self.queue) != 0
