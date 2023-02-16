class MyQueueSized:
    def __init__(self, number_max):
        self.items = [None] * number_max
        self.max_size = number_max
        self.head = 0
        self.tail = 0
        self.size_queue = 0


    def is_empty(self):
        return self.size_queue == 0


    def push(self, item):
        if self.size_queue != self.max_size:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size_queue += 1
            return 'OK'
        else:
            return print('error')


    def pop(self):
        if self.is_empty():
            return print('None')
        x = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_queue -= 1
        return print(x) 
    

    def peek(self):
        if self.is_empty():
            return print('None')
        x = self.items[self.head]
        return print(x)


    def get_size(self):
        if len(self.items) == 0:
            print(None)
        else:
            print(self.size_queue)


number_commands = int(input())
number_max = int(input())
queue = MyQueueSized(number_max)


for _ in range(number_commands):
    input_commands = input().split()

    if input_commands[0] == 'push':
        queue.push(int(input_commands[1]))

    if input_commands[0] == 'peek':
        queue.peek()
 
    if input_commands[0] == 'pop':
        queue.pop()
        
    if input_commands[0] == 'size':
        queue.get_size()
