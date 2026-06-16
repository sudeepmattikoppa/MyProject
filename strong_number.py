import math

# Input from user
num = int(input("Enter a number: "))

# Store original number
original_num = num

# Calculate sum of factorials of digits
sum_factorials = 0

while num > 0:
    digit = num % 10
    sum_factorials += math.factorial(digit)
    num //= 10

# Check if it is a Strong Number
if sum_factorials == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")
