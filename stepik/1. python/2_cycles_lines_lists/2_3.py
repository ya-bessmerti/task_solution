# a, b = (int(i) for i in input().split())
# s=0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     if i % 2 == 1:
#         s += i
# print(s)
def arithmetic_means(fist_number, second_number):
    general_list = []
    for item in range(fist_number, second_number + 1):
        if item % 3 == 0:
            general_list.append(item)
    arithmetic_mean = sum(general_list) / len(general_list)
    return arithmetic_mean

if __name__=='__main__':
    fist_number = int(input())
    second_number = int(input())
    print(arithmetic_means(fist_number, second_number))
