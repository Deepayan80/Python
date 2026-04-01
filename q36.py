# Write a recursive function to print all elements in a list. Hint: use list and index as parameters.

def print_list_recursive(lst, index=0):
    """
    Recursively print all elements in a list.
    
    Args:
        lst: The list to print
        index: Current index in the list (default is 0)
    """
    # Base case: if index is out of bounds, stop recursion
    if index >= len(lst):
        return
    
    # Print the current element
    print(lst[index])
    
    # Recursive case: move to the next index
    print_list_recursive(lst, index + 1)


# Test the function
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Printing list recursively:")
    print_list_recursive(numbers)
    
    print("\nAnother test:")
    fruits = ["apple", "banana", "orange", "mango"]
    print_list_recursive(fruits)
