def main(list_keyboard):
    result = list_keyboard[0]
    for x in range(1, len(list_keyboard)):
        cur_len = len(list_keyboard[x])
        ott_str = list()
        for i in range(len(result)):
            cur_out = [result[i]] * cur_len
            for j in range(cur_len):
                cur_out[j] = cur_out[j] + list_keyboard[x][j]
            ott_str.extend(cur_out)
        result = ott_str
    print(*result)


if __name__ == '__main__':
    number = str(input())
    list_number = []
    for item in number:
        list_number.append(item)
    keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    list_keyboard = []
    for index in range(len(list_number)):
        for i in list_number[index]:
            list_keyboard.append(keyboard[i])
    main(list_keyboard)
