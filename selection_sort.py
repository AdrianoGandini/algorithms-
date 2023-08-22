# Initial unsorted list
list = [10, 8, 7, 3, 2, 1]

# Function to perform selection sort
def selection_sort(list):
    list_length = len(list)

    # Outer loop: Iterate through each element up to the second-to-last element
    for i in range(0, list_length - 1):

        # Assume the current index has the minimum value
        min_index = i

        # Inner loop: Find the index of the minimum value in the unsorted portion
        for j in range(i + 1, list_length):
            # Compare the element at index j with the current minimum element
            if list[j] < list[min_index]:
                min_index = j

        # Swap the minimum element found with the element at the current index i
        list[i], list[min_index] = list[min_index], list[i]
    
    # Return the sorted list
    return list

# Call the selection_sort function and print the sorted list
print(selection_sort(list))

      