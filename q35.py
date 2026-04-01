# Write a recursion function to calculate the sum of first n natural numbers.
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

n = int(input("you want the sum of natural numbers: "))
print("The sum of first", n, "natural numbers is", sum_natural(n) )
