from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    number_list = []
    
    a = row + 1
    b = col
    if a < len(matrix):
        number_list.append (matrix[a][b])
    
    a = row - 1
    b = col
    if a > -1:
        number_list.append (matrix[a][b])

    a = row
    b = col +1
    if b < len(matrix[a]):
        number_list.append (matrix[a][b])
    
    a = row
    b = col - 1
    if b > -1:
        number_list.append (matrix[a][b])
    
    return number_list

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(*sorted(get_neighbours(matrix, row, col)))

