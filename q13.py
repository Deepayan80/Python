# Write a program to check if a list contains a palindrome of elements. (Hint: use copy() method.)
def is_palindrome(lst):
    # Create a copy of the original list
    lst_copy = lst.copy()
    
    # Reverse the copied list
    lst_copy.reverse()
    
    # Check if the original list is equal to the reversed copy
    return lst == lst_copy  

# Example usage
my_list = [1, 2, 3, 2, 1]
print(is_palindrome(my_list))  # Output: True