class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size += 1
    def pop(self):
        e = self.stack.pop()
        self.size -= 1
        return e

class SetOfStacks():
    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks = [Stack()]
        self.curr_stack = 0

    def push(self, item):
        if self.stacks[self.curr_stack].size == self.max_size:
            self.stacks.append(Stack())
            self.curr_stack += 1
        self.stacks[self.curr_stack].push(item)
    def pop(self):
        if  self.stacks[self.curr_stack].size == 0:
            if self.curr_stack > 0:
                self.curr_stack -= 1
            else:
                raise Exception("All stacks empty")
        e = self.stacks[self.curr_stack].pop()
        return e




def test_stacks():
    sos = SetOfStacks(2)
    for i in range(10):
        sos.push(1)
    for i in range(5):
        print(sos.stacks[i].stack)
    print(sos.curr_stack)
    for i in range(10):
        print(sos.pop())
test_stacks()
