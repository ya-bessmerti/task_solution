#ID 82764747
class Deque():
    def __init__(self, number_max):
        self.__items = [None] * number_max
        self.__max_size = number_max
        self.__head = 0
        self.__tail = -1
        self.__size_deque = 0

    def __is_empty(self):
        return self.__size_deque == 0

    def __move_pointer(self, pointer, direction):
        if direction:
            return (pointer + 1) % self.__max_size
        return (pointer - 1) % self.__max_size

    def push_back(self, item):
        if self.__size_deque != self.__max_size:
            self.__tail = self.__move_pointer(
                self.__tail,
                direction=True,
            )
            self.__items[self.__tail] = item
            self.__size_deque += 1
        else:
            raise OverflowError

    def push_front(self, item):
        if self.__size_deque != self.__max_size:
            self.__head = self.__move_pointer(
                self.__head,
                direction=False,
            )
            self.__items[self.__head] = item
            self.__size_deque += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.__is_empty():
            raise IndexError
        pop_back_number = self.__items[self.__tail]
        self.__items[self.__tail] = None
        self.__tail = self.__move_pointer(
            self.__tail,
            direction=False,
        )
        self.__size_deque -= 1
        return pop_back_number

    def pop_front(self):
        if self.__is_empty():
            raise IndexError
        pop_front_number = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = self.__move_pointer(
            self.__head,
            direction=True,
        )
        self.__size_deque -= 1
        return pop_front_number


def main():
    number_commands = int(input())
    number_max = int(input())
    deque = Deque(number_max)
    for _ in range(number_commands):
        input_commands = input().split(' ')
        operation, *value = input_commands
        if value:
            try:
                result = getattr(deque, operation)(int(*value))
            except OverflowError:
                print('error')
        else:
            try:
                result = getattr(deque, operation)()
                print(result)
            except IndexError:
                print('error')


if __name__=='__main__':
    main()
