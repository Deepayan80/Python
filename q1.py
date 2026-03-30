pa = int(input("Enter the principal amount: "))
if pa < 1000:
    dis = pa * 0.95
elif pa >= 1000 and pa < 5000:  
    dis = pa * 0.90
else:
    dis = pa * 0.85
print("The amount to be paid after discount is: ", format(dis, ".2f"))