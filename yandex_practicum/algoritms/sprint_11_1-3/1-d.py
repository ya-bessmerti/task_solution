from typing import List

def get_weather_randomness(temperatures: List[int], n: int) -> int:
    randomness = 0
    for i in range(1, n- 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            randomness += 1
    try:
        if temperatures[0] > temperatures[1]:
            randomness += 1
        if temperatures[-1] > temperatures[-2]:
            randomness += 1
    except IndexError:
        randomness += 1
    return randomness
    

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures, n

temperatures, n = read_input()
print(get_weather_randomness(temperatures, n))