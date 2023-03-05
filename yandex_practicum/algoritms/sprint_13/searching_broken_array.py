#ID 83448959
from typing import List


def broken_search(array: List[int], target: int) -> int:
    left_index, right_index = 0, len(array) - 1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if target == array[middle_index]:
            return middle_index
        if array[left_index] <= array[middle_index]:
            if array[left_index] <= target <= array[middle_index]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        else:
            if array[middle_index] <= target <= array[right_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
    return -1


def main() -> None:
    _ = int(input())
    desired_element = int(input())
    array = [int(i) for i in input().strip().split()]
    print(broken_search(array, desired_element))


if __name__ == '__main__':
    main()
