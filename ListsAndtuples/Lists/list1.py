# This is a simple Python script that populates a list with integers from 1 to 10.

# Initialize an empty list.
l = []

# Use a for loop to iterate over a range of numbers from 1 to 11.
for i in range(1, 11):
    # Append each number to the list.
    l.append(i)

# Print the populated list.
print(l)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("--------------")

# Initialize an empty list.
l = []

# Initialize a counter variable.
i = 1

# Use a while loop to iterate until i is less than or equal to 10.
while i <= 10:
    # Append each number to the list.
    l.append(i)
    # Increment the counter.
    i += 1

# Print the populated list.
print(l)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("--------------")
l = []
i = 1
while True:
    l.append(i)
    i += 1
    if i > 10:
        break
print(l)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("--------------")
# Initialize an empty list.
l = []

# Use a list comprehension to generate the list of numbers from 1 to 10.
l = [i for i in range(1, 11)]

# Print the populated list.
print(l)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("--------------")
