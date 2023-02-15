class StackMax:
    def __init__(self):
        self.items = []
        
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            return 'error'
        else:
            return self.items.pop()
    
    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return max(self.items)


number = int(input())
stack = StackMax()
task = []
for _ in range(number):
    input_commands = input().split()
    if input_commands[0] == "push":
        stack.push(int(input_commands[1]))
 
    if input_commands[0] == "pop":
        if stack.pop() == 'error':
            task.append('error')
        
    if input_commands[0] == "get_max":
        task.append(stack.get_max())
 
for i in task:
    print(i)
