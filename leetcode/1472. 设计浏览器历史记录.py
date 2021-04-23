class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.stack.append(homepage)
        self.index = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.index + 1]
        self.stack.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0: self.index = 0
        return self.stack[self.index]

    def forward(self, steps: int) -> str:
        self.index += steps
        if self.index >= len(self.stack): self.index = len(self.stack) - 1
        return self.stack[self.index]
