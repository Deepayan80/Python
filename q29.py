# Write a program to find sum of first n numbers.
n = int(input("Enter the last number this which sum you want: "))
i = 0;
sum = 0;
while i != n:
    sum += i;
    i += 1;
print("The sum is : ", sum)