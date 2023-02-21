#ID 82761807
import math


class ItemsAreMissingException(Exception):
    def __init__(self):
        pass


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if len(self.__items) != 0:
            return self.__items.pop()
        raise ItemsAreMissingException


def calculate(input_items):
    dictionary_calculations = {
        '+':lambda second_summand, first_summand: (
            first_summand + second_summand
        ),
        '-':lambda deductible, reduced: (
            reduced - deductible
        ),
        '/':lambda denominator, numerator: math.floor(
            numerator/denominator
        ),
        '*':lambda second_factor, first_factor: (
            first_factor * second_factor
        ),
    }
    stack = Stack()
    for value in input_items.split():
        try:
            stack.push(int(value))
        except ValueError:
            stack.push(
                dictionary_calculations[value](
                    stack.pop(),stack.pop()
                )
            )
    return stack.pop()


if __name__=='__main__':
    print(calculate(input()))
