# Search for number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
mytup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number you want to search in this tupple: "))
idx = 0
for i in mytup:
    if x == i:
        print("Element found at indx: ", idx)
        break
    idx += 1
else:
    print("Element not found in the tuple.")

print("End of Search")
