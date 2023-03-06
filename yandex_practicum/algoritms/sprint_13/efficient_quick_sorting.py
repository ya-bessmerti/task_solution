#ID 83531762
def quick_sort(array, left, right):
    if right <= left:
        return
    left_index = left
    right_index = right
    pivot = (left + right) // 2
    reference = array[pivot]
    while left_index <= right_index:
        while reference > array[left_index]:
            left_index += 1
        while reference < array[right_index]:
            right_index -= 1
        if left_index <= right_index:
            array[left_index], array[right_index] = (array[right_index],
                                                     array[left_index])
            left_index += 1
            right_index -= 1
    quick_sort(array, left, right_index)
    quick_sort(array, left_index, right)


def read_input(index):
        name, points, penalty = input().split()
        players[index] = (-int(points), int(penalty), name)
        return players[index]


if __name__ == '__main__':
    count_line = int(input())
    players = [None] * count_line
    players = [read_input(index) for index in range(count_line)]
    quick_sort(players, 0, len(players) - 1)
    [print(row[2]) for row in players]
