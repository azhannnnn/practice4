# stack

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def rev_str(str1):
    reverse = ""

    s = Stack()
    for i in str1:
        s.push(i)

    while not s.is_empty():
        reverse += s.pop()

    return reverse

str1 = input("enter the string : ")

print(rev_str(str1))