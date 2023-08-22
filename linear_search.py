#Linear Search unsorted list 
list = [10, 8, 7, 3, 2, 1]

def linear_search (list, element):
    
    for item in list:
      if item == element:
         return True
    return False

print(linear_search(list, 7))