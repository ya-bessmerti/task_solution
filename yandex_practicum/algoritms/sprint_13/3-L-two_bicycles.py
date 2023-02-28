def piggy_bank(money_list, cost_bicycle, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money_list[middle] >= cost_bicycle and (money_list[middle - 1] < cost_bicycle or middle == 0)):
        return middle + 1
    elif cost_bicycle <= money_list[middle]:
        return piggy_bank(money_list, cost_bicycle, left, middle)
    else:
        return piggy_bank(money_list, cost_bicycle, middle + 1, right)
    

if __name__=='__main__':
    number_days = int(input())
    money_list = list(map(int, input().strip().split()))
    cost_bicycle = int(input())
    first_day = (piggy_bank(money_list, cost_bicycle, left=0, right=len(money_list)))
    second_day = (piggy_bank(money_list, cost_bicycle*2, left=0, right=len(money_list)))
    print(first_day, second_day)
