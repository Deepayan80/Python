# Write a function to print the length of a list.
def length(myList= []):
    a = len(myList)
    return a

mylist = [1,20,3,0,1,0,5,0,7]
print("The length of the list is: ", length(mylist))