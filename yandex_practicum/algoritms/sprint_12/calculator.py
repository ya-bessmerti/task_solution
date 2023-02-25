#ID 82890990
class ItemsAreMissingException(Exception):
    pass


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if self.__items:
            return self.__items.pop()
        raise ItemsAreMissingException


def calculate(input_items):
    dictionary_calculations = {
        '+': lambda b, a: a + b,
        '-': lambda b, a: a - b,
        '/': lambda b, a: a // b,
        '*': lambda b, a: a * b,
    }
    stack = Stack()
    for value in input_items.split():
        try:
            stack.push(
                dictionary_calculations[value](stack.pop(),stack.pop())
            )
        except KeyError:
            stack.push(int(value))
    return stack.pop()


if __name__=='__main__':
    print(calculate(input()))
