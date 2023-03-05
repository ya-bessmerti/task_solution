def subsequence(first_string, second_string):
    index = -1
    for item in first_string:
        index = second_string.find(item, index + 1)
        if index == -1:
            return False
    return True


if __name__=='__main__':
    first_string = str(input())
    second_string = str(input())
    print(subsequence(first_string, second_string))