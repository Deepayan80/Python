# Write a function to find the factorial of n.
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

n = int(input("Enter the number whose factorial you want: "))
print("The fact of number: ", fact(n))