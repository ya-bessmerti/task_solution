from typing import List

def get_distance(number_houses: List[int], n: int) -> int:
    list_zero = []
    for i in range(n):
        if number_houses[i] == 0:
             list_zero.append(i)
    
    result = [0] * n

    for house in range(0, list_zero[0] + 1):
        result[house] = list_zero[0] - house
    
    for position in range(len(list_zero) - 1):
        zero_1, zero_2 = list_zero[position], list_zero[position + 1]
        
        for house in range(zero_1, zero_2):
            result[house] = min(house - zero_1, zero_2 - house)
    
    for house in range(list_zero[-1], n):
        result[house] = house - list_zero[-1]
    
    return result


def read_input() -> List[int]:
    n = int(input())
    number_houses = list(map(int, input().strip().split()))
    return number_houses, n

number_houses, n = read_input()

print(' '.join(map(str, get_distance(number_houses, n))))
