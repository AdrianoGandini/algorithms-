#Binary search algorithm

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def binary_search(list, item):

    low = 0
    high = len(list) - 1
    found = False

    while low <= high and not found:
        list_midle = (low + high) // 2
        if list[list_midle] == item:
            found = True
        elif item < list[list_midle]:
            high = list_midle - 1
        else:
            low = list_midle  + 1

    return found

print(binary_search(list, 7))