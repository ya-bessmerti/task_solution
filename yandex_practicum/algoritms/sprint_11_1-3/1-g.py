def to_binary(number: int) -> str:
    binary = ''
    if number == 0:
        return f'0'
    else:
        while number >= 1:
            res = number // 2
            binary += str(number % 2)
            number = res
        return binary[::-1]

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))