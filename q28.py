# Prints all elements but not multiple of 3:
for i in range(1000):
    if i % 3 == 0:
        continue
    else:
        print(i)