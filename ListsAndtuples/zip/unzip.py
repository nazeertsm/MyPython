"""""""""
Unzipping in Python refers to the process of separating combined sequences, 
which have been previously zipped together using the zip() function. Essentially, 
if you have a sequence of tuples where each tuple contains elements from different iterables, 
unzipping will extract these original sequences back from the tuples.
You can achieve unzipping using the zip() function combined with the unpacking operator *, 
which is often referred to as the "splat" operator.

Example:
Continuing from the earlier example where we had zipped together names and ages
"""""""""
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
paired = zip(names, ages)
paired_list = list(paired)
#Suppose paired has been converted to a list and looks like this:
print(list(paired))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

#Now, let's unzip this list back into two lists:
unzipped = zip(*paired_list)
names_unzipped, ages_unzipped = list(unzipped)
print(names_unzipped)  # Output: ('Alice', 'Bob', 'Charlie')
print(ages_unzipped)  # Output: (25, 30, 35)

"""""""""""
Unzipping is useful when you need to distribute a collection of tuples into separate sequences, 
which can be particularly useful in data processing where combined data needs to be separated 
for individual processing tasks. This method allows for straightforward and clean extraction of 
original datasets from a zipped aggregate.
"""""""""""
