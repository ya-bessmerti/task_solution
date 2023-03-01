def gen_binary(control, first_number, second_number, prefix):
    if first_number == 0 and second_number == 0:
        print(prefix)
    else:
        if first_number > 0:
            gen_binary(control + 1, first_number - 1, second_number, prefix + '(')
        if (control > 0 and second_number > 0):
            gen_binary(control - 1, first_number, second_number - 1, prefix + ')')
    


if __name__ == '__main__':
    number = int(input())
    control = 0
    first_number = number
    second_number = number
    gen_binary(control, first_number, second_number, '')
