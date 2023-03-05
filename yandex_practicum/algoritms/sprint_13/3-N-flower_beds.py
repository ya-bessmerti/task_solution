from typing import List

def merge_flower_beds(gardeners, beds):
    result = []
    beds = sorted(beds, key=lambda i: [i[0], i[1]])
    for i in range(gardeners-1):
        if (beds[i][1] >= beds[i+1][0]):
            beds[i+1][0] = min(beds[i][0], beds[i+1][0])
            beds[i+1][1] = max(beds[i][1], beds[i+1][1])
        else:
            result.append(beds[i])
    result.append(beds[-1])
    return result

def main():
    gardeners = int(input())
    flower_beds = [[int(i) for i in input().split()] for _ in range(gardeners)]
    result = merge_flower_beds(gardeners, flower_beds)
    [print(*i) for i in result]


if __name__ == '__main__':
    main()