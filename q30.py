# Write a program to find the factorial of first n numbers. 
n = int(input("Enter the number whose factorial you want: "))
fact = 1
i = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of", n, "is:", fact)