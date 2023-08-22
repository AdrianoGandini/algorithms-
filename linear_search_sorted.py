#Linear Search sorted list
list = [1, 2, 8, 10, 13, 15, 18, 20]


def search_ordered_list (list, element):

    index = 0
    found = False
    stop = False

    while index < len(list) and not found and not stop:
        if list[index] == element:
            found = True
        elif list[index] > element:
            stop = True
        else:
            index += 1

    return found

print(search_ordered_list(list, 21))
