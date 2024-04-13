"""""""""""
The zip() function in Python is used to combine multiple iterable objects (like lists or tuples)
into a single iterable of tuples. Each tuple contains elements from the iterables passed to zip()
that are in the same position. Here's a step-by-step explanation with an example:
Example:
Suppose we have two lists: one with names and another with ages. We want to pair each name with its corresponding age
"""""""""""

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

#We can use zip() to pair these lists together:
pairs = zip(names, ages)
print(list(pairs))

"""""""""""
#Practical Use:
#You can directly iterate over the zip object in a loop,
#which is useful in scenarios where you need to use paired data, such as displaying names with ages
"""""""""""
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')
