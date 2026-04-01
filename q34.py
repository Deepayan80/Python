# Write a function to convert usd to inr.
def INR(USD):
    inr = USD * 93.23
    return inr

usd = float(input("Enter amount in usd: "))
print(usd, "$ is equal to ₹ ", INR(usd))
