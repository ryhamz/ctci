class MultiStack:

    def __init__(self, size):
        self.numstacks = 3
        self.array = [0] * (size * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.size = size

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('No space available in stack %d', stacknum)

        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception("No items in stack %d", stacknum)

        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.size

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.size
        return offset + self.sizes[stacknum] - 1

def ThreeInOne():
    s = MultiStack(5)
    print(s.IsEmpty(1))
    s.Push(3, 1)
    print(s.Peek(1))
    print(s.IsEmpty(1))
    s.Push(2, 1)
    print(s.Peek(1))
    print(s.Pop(1))
    print(s.Peek(1))
    s.Push(3, 1)

ThreeInOne()
