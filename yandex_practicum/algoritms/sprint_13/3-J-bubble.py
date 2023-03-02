def bubble_sort(number, number_list):
    printed = 0
    for i in range(number-1):
        sorted = 0
        for index in range(number-1-i):
            if number_list[index] > number_list[index+1]:
                number_list[index], number_list[index+1] = number_list[index+1], number_list[index]
                sorted += 1
        if sorted:
            printed += 1
            print(*number_list)
    if not printed:
        print(*number_list)


if __name__=='__main__':
    number = int(input())
    number_list = list(map(int, input().split()))
    bubble_sort(number, number_list)