#ID 82708404
import math


class Calculator():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        raise 'error'


def get_items(values):
    for value in values:
        try:
            calculator.push(int(value))
        except ValueError:
            if value == '+':
                calculator.push(
                    (calculator.pop()) + (calculator.pop())
                )
            if value == '-':
                get_lambda = lambda deductible, reduced: reduced - deductible
                calculator.push(
                    int(
                        get_lambda(calculator.pop(), calculator.pop())
                    )
                )
            if value == '/':
                get_lambda = lambda denominator, numerator: math.floor(
                    numerator/denominator
                )
                calculator.push(
                    int(get_lambda(calculator.pop(), calculator.pop()))
                )
            if value == '*':
                calculator.push((calculator.pop()) * (calculator.pop()))


if __name__=='__main__':
    input_items = input().split()
    calculator = Calculator()
    get_items(input_items)
    print(calculator.pop())
