def gen_binary(list_number, dict_keyboard):
    if first_number == 0 and second_number == 0:
        print(prefix)
    else:
        if first_number > 0:
            gen_binary(control + 1, first_number - 1, second_number, prefix + '(')
        if (control > 0 and second_number > 0):
            gen_binary(control - 1, first_number, second_number - 1, prefix + ')')
    pass


if __name__ == '__main__':
    number = str(input())
    list_number = []
    for item in number:
        list_number.append(item)
    keyboard = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    dict_keyboard = {}
    for index in range(len(list_number)):
        for i in list_number[index]:
            y = {i: keyboard[i]}
            dict_keyboard.update(y)
    print(list_number)
    print(dict_keyboard)
    gen_binary(list_number, dict_keyboard)
