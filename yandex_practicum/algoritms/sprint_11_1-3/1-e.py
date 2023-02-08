def get_longest_word(line: str) -> str:
    line = line.strip().split()
    longest = 0
    for i in range(1, len(line)):
        if len(line[i]) > len(line[longest]):
            longest = i
    return line[longest]

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))