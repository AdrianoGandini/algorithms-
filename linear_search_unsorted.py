#Lienar Search unsorted list

list = [2, 10, 8, 15, 18, 20, 12, 1]

def linear_search_unsorted(list, element):

    index = 0
    found = False

    while index < len(list) and not found:
        if element == list[index]:
            found = True
        else:
            index += 1

    return found

print(linear_search_unsorted(list, 30))