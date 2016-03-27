# Uses python3

# Calculate the maximum value of multiplication of two integers in given numbers

# Take the number of integers
n = int(input())

# Split input and assign it to a as an integer
a = [int(x) for x in input().split()]

# Control if number of integers equal to input
assert(len(a) == n)

# First assignment of index
max1 = -1
max2 = -1

# Find the maximum integer in set
for i in range(0, n):
    if max1 == -1 or a[i] > a[max1]:
        max1 = i

# Find the second maximum integer in set
for i in range(0, n):
    if i != max1 and (max2 == -1 or a[i] > a[max2]):
        max2 = i

# Multiplication
print(a[max1]*a[max2])