import math

class Calculator():
    def __init__(self):
        self.items = []

    
    def push(self, item):
        self.items. append(item)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return 'error'


if __name__=='__main__':
    
    input_items = input().split()
    calculator = Calculator()
    for value in input_items:
        try:
            calculator.push(int(value))
        except ValueError:
            if value == '+':
                calculator.push((calculator.pop()) + (calculator.pop()))
            if value == '-':
                calculator.push((calculator.pop()) - (calculator.pop()))
            if value == '/':
                calculator.push((calculator.pop()) / (calculator.pop()))
            if value == '*':
                calculator.push((calculator.pop()) * (calculator.pop()))
    print(calculator.pop())







    # operations = []
    # numbers_list = []
    # for element in  input_item:
    #     if element == '+' or element == '-' or element == '*' or element == '/':
    #         operations.append(element)
    #     else:
    #         numbers_list.append(int(element))
    # calculator = Calculator(operations)
    # print (calculator.get_operations(numbers_list, operations))

