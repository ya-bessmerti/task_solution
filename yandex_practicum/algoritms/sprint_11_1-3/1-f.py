def is_palindrome(line: str) -> bool:
    line = ''.join(filter(str.isalpha, line.lower()))
    reversed_text = line[::-1]
    return line == reversed_text

print(is_palindrome(input().strip()))