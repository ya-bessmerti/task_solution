#ID 82032290
from typing import List


def get_distance(
    number_houses: List[int],
    street_length: int,
) -> int:
    list_zero = [
        zero_search
        for zero_search in range(street_length)
        if number_houses[zero_search] == 0
    ]
    result = [0] * street_length
    for house in range(0, list_zero[0] + 1):
        result[house] = list_zero[0] - house
    for position in range(len(list_zero) - 1):
        empty_plot = list_zero[position]
        next_empty_section = list_zero[position + 1]
        for house in range(empty_plot, next_empty_section):
            result[house] = min(
                house - empty_plot,
                next_empty_section - house
            )
    for house in range(list_zero[-1], street_length):
        result[house] = house - list_zero[-1]
    return result


if __name__=='__main__':
    street_length = int(input())
    number_houses = list(map(int, input().strip().split()))
    result_list = get_distance(number_houses, street_length)
    print(*result_list, sep=' ')
