class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.queue1) == 0:
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) == 0:
            num = self.queue2.pop(0)
        else:
            num = self.queue1.pop(0)
        return num


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue1) == 0: return self.queue2[0]
        if len(self.queue2) == 0: return self.queue1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0
