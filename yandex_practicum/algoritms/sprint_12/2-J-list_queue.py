class MyQueueSized:
    def __init__(self):
        self.items = []

    def put(self, item):
        return self.items.append(item)


    def get(self):
        if len(self.items) == 0:
            return print('error')
        x = self.items[0]
        self.items.pop(0)
        return print(x) 


number_commands = int(input())
queue = MyQueueSized()


for _ in range(number_commands):
    input_commands = input().split()

    if input_commands[0] == 'put':
        queue.put(int(input_commands[1]))

    if input_commands[0] == 'get':
        queue.get()

    if input_commands[0] == 'size':
        print(len(queue.items))
