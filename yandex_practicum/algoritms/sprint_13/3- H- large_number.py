def lurge_number(number, number_list):
    for index in range(1, number):
        item_to_insert = number_list[index]
        j = index
        while j > 0 and compare(item_to_insert, number_list[j - 1]):
            number_list[j] = number_list[j - 1]
            j -= 1
        number_list[j] = item_to_insert
    return ''.join(number_list[::-1])


def compare(obj_1: str, obj_2: str) -> bool:
    if int(obj_1 + obj_2) < int(obj_2 + obj_1):
        return True
    return False


if __name__=='__main__':
    number = int(input())
    number_list = list(map(str, input().strip().split()))
    print(lurge_number(number, number_list))