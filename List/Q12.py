#Queue

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return not self.items
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
# if __name__ == "__main__":
q = Queue()
print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.peek())
print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q)
q.enqueue(1)
q.enqueue(2)
print(q)
