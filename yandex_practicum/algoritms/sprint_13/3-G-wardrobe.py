def  counting_sort(color_list, k = 3):
    counted_values = [0] * k
    for value in color_list:
        counted_values[value] += 1
        
    for color in range(k):
        print((str(color) + ' ') * counted_values[color], end='')


if __name__=='__main__':
    number = int(input())
    color_list = [int(i) for i in input().strip().split()]
    counting_sort(color_list)