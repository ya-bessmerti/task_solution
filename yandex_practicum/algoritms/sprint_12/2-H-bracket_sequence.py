class Stack:    
    def __init__(self):
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


line = list(input())
standard = {'(':')','{':'}','[':']'}
stack = Stack()

for item in line:
    if item in standard.keys():
        stack.push(item)
    elif not stack.isEmpty() and standard[stack.peek()] == item:
        stack.pop()
    else:
        stack.push(item)
        break

if stack.isEmpty():    
    print(True)
else:
    print(False)
