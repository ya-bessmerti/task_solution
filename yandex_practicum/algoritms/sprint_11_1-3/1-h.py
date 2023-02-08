from itertools import zip_longest
from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    summ = ''
    carry_one = 0
    if second_number == '0':
        return first_number
    else:

        for arr in zip_longest(first_number[::-1], second_number[::-1], fillvalue='0'):
            temp_sum = int(arr[0]) + int(arr[1]) + carry_one
            summ += str(temp_sum % 2)
            carry_one = temp_sum // 2
        if carry_one:
            summ += '1'
        return summ[::-1]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))