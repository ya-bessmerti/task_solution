from math import sqrt
from typing import List

def factorize(number: int) -> List[int]:
    result  = []
    for i in range(2, int(sqrt(number))+1):
        while number % i == 0:
            result.append(i)
            number = number // i
            if number == 1:
                break

    if number > 1:
        result.append(number)
    return result

result = factorize(int(input()))
print(" ".join(map(str, result)))