class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []


    def push(self, item):
        if len(self.items) == 0:
            self.items.append(item)
            self.max_items.append(item)
        else:
            self.items.append(item)
            if item > self.max_items[-1]:
                self.max_items.append(item)
            else:
                self.max_items.append(self.max_items[-1])


    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            return self.items.pop(), self.max_items.pop()
    
    def get_max(self):
        if len(self.items) == 0:
            print(None)
        else:
            print(self.max_items[-1])


number = int(input())
stack = StackMaxEffective()


for _ in range(number):
    input_commands = input().split()
    if input_commands[0] == 'push':
        stack.push(int(input_commands[1]))
 
    if input_commands[0] == 'pop':
        stack.pop()
        
    if input_commands[0] == 'get_max':
        stack.get_max()
