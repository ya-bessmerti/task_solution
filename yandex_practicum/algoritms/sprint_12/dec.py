class Dec:
    def __init__(self, number_max):
        self.items = [None] * number_max
        self.max_size = number_max
        self.head = 0
        self.tail = 0
        self.size_dec = 0


    def is_empty(self):
        return self.size_dec == 0


    def push_back(self, item):
        if self.size_dec != self.max_size:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size_dec += 1
            return 'OK'
        else:
            return print('error')


    def push_front(self, item):
        if self.size_dec != self.max_size:
            self.items[self.head] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size_dec += 1
            return 'OK'
        else:
            return print('error')


    def pop_back(self):
        if self.is_empty():
            return print('error')
        pop_number = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_dec -= 1
        return print(pop_number)

    def pop_front(self):
        if self.is_empty():
            return print('error')
        pop_number = self.items[self.tail]
        self.items[self.tail] = None
        self.tail = (self.tail + 1) % self.max_size
        self.size_dec -= 1
        return print(pop_number) 


number_commands = int(input())
number_max = int(input())
dec = Dec(number_max)


for _ in range(number_commands):
    input_commands = input().split()

    if input_commands[0] == 'push_back':
        dec.push_back(int(input_commands[1]))
    
    if input_commands[0] == 'push_front':
        dec.push_front(int(input_commands[1]))

    if input_commands[0] == 'pop_front':
        dec.pop_front()

    if input_commands[0] == 'pop_back':
        dec.pop_back()
