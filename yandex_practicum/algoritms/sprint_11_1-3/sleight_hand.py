#ID 82035722
from collections import Counter
from typing import List, Union


def get_simulator_printings(
    number_keys: int,
    field: List[Union[int, str]],
) -> int:
    result = 0
    field_in_line = Counter([
        item
        for field_string in field
        for item in field_string
    ])
    dict_field = dict(field_in_line)
    dict_field.pop('.', None)
    for item in dict_field.values():
        if item <= 2*number_keys:
            result +=1
    return result


if __name__=='__main__':
    number_keys = int(input())
    field = [
        input().strip()
        for _ in range(4)
    ]
    print((get_simulator_printings(number_keys, field)))
