# Solution verified on Leetcode problem #155.
class Minstack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, element):
        self.stack.append(element)
        if not self.minstack or element <= self.minstack[-1]:
            self.minstack.append(element)
    def pop(self):
        e = self.stack.pop()
        if self.minstack and e == self.minstack[-1]:
            self.minstack.pop()
        return e
    def min(self):
        return self.minstack[-1]

