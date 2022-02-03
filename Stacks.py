class Stacks:
    """attributes"""

    def __init__(self, size):
        self.top = -1
        self.container = []
        limit = 6
        self.size = size

        """checking if the given size is greater the limit asigned"""
        if self.size > limit:
            print("Provided size of stacks limit of {0}. size is now {1}".format(limit, limit))
            self.size = limit

    """methods"""

    def push(self, x):
        if self.is_full():
            print("Is Full")
            return
        else:
            self.container.append(x)
            self.top += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            exiting = self.container[self.top]
            self.container.pop(self.top)
            self.top -= 1
            return exiting

    def is_empty(self):
        """returns a boolean ie True or False (more like an if statement)"""
        return self.top < 0

    def is_full(self):
        return len(self.container) >= self.size  # returns another boolean if the stack is full

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.container[self.top]

    def snap(self):
        print(self.container)


my_stack = Stacks(10)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
my_stack.push(8)
my_stack.push(9)
my_stack.snap()
my_stack.push(3)
my_stack.snap()
my_stack.push(3)
my_stack.snap()