class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for cur in asteroids:
            stack.append(cur)
            self.helper(stack)
        return stack

    def helper(self, stack):
        while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
            cur = stack.pop()
            pre = stack.pop()
            if -cur != pre:
                res = pre if pre > -cur else cur
                stack.append(res)
