import math


class Calculator():
    def __init__(self, operations):
        self.items = [None] * len(operations)
        self.head = 0
        self.tail = -1
        self.size_dec = 0

    
    def get_operations(self, numbers_list, operations):
        for item in range(len(operations)):
            if operations[item] == '+':
                numbers_list[item+1] = numbers_list[item] +  numbers_list[item+1]
                numbers_list[item] = None

            if operations[item] == '-':
                numbers_list[item+1] = numbers_list[item] -  numbers_list[item+1]
                numbers_list[item] = None
            if operations[item] == '*':
                numbers_list[item+1] = numbers_list[item] *  numbers_list[item+1]
                numbers_list[item] = None
            if operations[item] == '/':
                numbers_list[item+1] = math.ceil(numbers_list[item] //  numbers_list[item+1])
                numbers_list[item] = None
        return int(numbers_list[-1])


if __name__=='__main__':
    
    input_item = input().split()
    operations = []
    numbers_list = []
    for element in  input_item:
        if element == '+' or element == '-' or element == '*' or element == '/':
            operations.append(element)
        else:
            numbers_list.append(int(element))
    calculator = Calculator(operations)
    print (calculator.get_operations(numbers_list, operations))

