# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as values.
myDict = {
    "Math": "",
    "English": "",
    "Science" : ""
}

myDict["Math"] = int(input("Enter maths marks: "))
myDict["English"] = int(input("Enter english marks: "))
myDict["Science"] = int(input("Enter science marks: "))

print(myDict)