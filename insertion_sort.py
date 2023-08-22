# Insertion sort algorithm

# Given list of numbers
list = [10, 8, 7, 3, 2, 1]

# Define the insertion_sort function
def insertion_sort(list):
    # Get the length of the list
    list_length = len(list)
    
    # Loop through the list, starting from the second element
    for i in range(1, list_length):
        # Store the value to be inserted
        insert_value = list[i]
        
        # Initialize j to the index before i
        j = i - 1
        
        # Compare and shift elements to the right until the correct position is found
        while j >= 0 and list[j] > insert_value:
            list[j + 1] = list[j]  # Shift the larger element to the right
            j -= 1
        
        # Insert the value in its correct position
        list[j + 1] = insert_value
        
    # Return the sorted list
    return list

# Call the insertion_sort function and print the sorted list
print(insertion_sort(list))

