from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = deque()
        self.stack2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.appendleft(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack2) == 0:
            val = self.stack1.pop()
            self.stack2.append(val)
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) == 0:
            val = self.stack1.pop()
            self.stack2.append(val)
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
