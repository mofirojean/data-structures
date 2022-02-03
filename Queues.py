"""Algorithm for Queues"""
class Queues:
    """attributes of the queue"""
    def __init__(self, length):
        self.front = -1
        self.back = -1
        self.container = []

        self.length = length

    """methods of a queue"""
    def is_empty(self):
        """testing the queue size"""
        return len(self.container) == 0

    """adding an element in a queue"""
    def enqueue(self, value):
        if self.is_empty():
            self.front += 1
            self.back += 1
        else:
            self.back += 1
        self.container.append(value)

    """removing the value fom a queue """
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            self.container.pop(self.front)
            self.back -= 1


    """declaring that a list is full"""
    def is_full(self):
        if len(self.container) >= self.length:
            print("is full")
            return True
        else:
            print("NO its not")
            return False

    """snapping the container"""
    def snap(self):
        print(self.container)


my_queue = Queues(3)
i = 6
my_queue.enqueue(1)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.snap()
my_queue.enqueue(3)
my_queue.snap()
my_queue.is_full()

my_queue.dequeue()
print(my_queue.back)
my_queue.snap()
