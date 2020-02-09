decimal_number = int(input())

remainders = ""
while decimal_number > 0:
    remainders += str(decimal_number % 2)
    decimal_number = int(decimal_number / 2)

# Reverse the remainder's array will give you the binary number.
# In this task it doesn't matter
consecutive_ones = remainders.split("0")

# Find the maximum of consecutive_ones
maximum = len(consecutive_ones[0])
for i in range(len(consecutive_ones)):
    if len(consecutive_ones[i]) > maximum:
        maximum = len(consecutive_ones[i])

print(maximum)
