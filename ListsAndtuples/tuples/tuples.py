"""""""""
Tuples are a fundamental data type in Python that are used to store immutable sequences of items.
This means that once a tuple is created, you cannot modify its contents—add or remove elements.
However, tuples can contain mutable objects, like lists. Tuples are defined by enclosing the elements in parentheses `( )`, 
although parentheses are optional in many contexts. Here’s a breakdown with examples to help you understand tuples better:
"""""""""
### Example 1: Creating a Simple Tuple

#Here is how you create a basic tuple containing several types of data:


my_tuple = (1, 'hello', 3.14)
print(my_tuple)  # Output: (1, 'hello', 3.14)


"""""""""
**Explanation**: This tuple `my_tuple` contains an integer, a string, and a floating-point number. 
Tuples can store data of different types.
"""""""""
print("--------------")

### Example 2: Tuple Without Parentheses

#Tuples can be created without parentheses, using just commas. This is known as tuple packing.


another_tuple = 'apple', 'banana', 'cherry'
print(another_tuple)  # Output: ('apple', 'banana', 'cherry')

"""""""""
**Explanation**: Python recognizes the commas as an indication to create a tuple, 
and `another_tuple` is treated as a tuple even without parentheses.
"""""""""
print("--------------")
### Example 3: Accessing Tuple Elements

#Elements in a tuple can be accessed via indexing, just like lists. Indexing starts at 0.


colors = ('red', 'green', 'blue')
print(colors[1])  # Output: green

#**Explanation**: `colors[1]` accesses the second element in the tuple `colors`, which is "green".
print("--------------")
### Example 4: Tuple Unpacking

#Tuple unpacking allows you to assign the elements of a tuple into variables in a single line.


data = (100, 'Jane Doe', 'New York')
id, name, city = data
print(name)  # Output: Jane Doe


#**Explanation**: The variables `id`, `name`, and `city` are assigned to the corresponding elements of the tuple `data`.
print("--------------")
### Example 5: Tuples in a Function

#Tuples are often used to return multiple values from a function.

def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple with min and max


result = get_min_max([4, 1, 17, 10, 6])
print("Min:", result[0], "Max:", result[1])  # Output: Min: 1 Max: 17

#**Explanation**: The function `get_min_max` returns a tuple containing the minimum and maximum values from a list of numbers.
print("--------------")
### Example 6: Tuples are Immutable

#Once created, the contents of a tuple cannot be altered.

# This will raise an error
t = (1, 2, 3)
#t[0] = 99  # Raises an error

#TypeError: 'tuple' object does not support item assignment

#**Explanation**: Trying to change an element of a tuple results in a `TypeError` because tuples are immutable.

### Usage

#Tuples are particularly useful when you need a function to return multiple values,
# when you want to create a constant set of values to iterate over, or when you require an immutable
# version of a list for a fixed sequence of elements. Their immutability makes them a safe choice for
# ensuring that data cannot be changed by mistake.

# The following Python code demonstrates the concept of tuple unpacking.

# A tuple is created with three elements: an integer, a string, and a floating-point number.
data = (12, "apple", 3.14)

# Tuple unpacking is used here to assign the values from the tuple to three variables: id, name, and price.
# The first element of the tuple (12) is assigned to 'id', the second element ("apple") to 'name', and the third element (3.14) to 'price'.
id, name, price = data

# The value of the 'name' variable is printed. As 'name' was assigned the value "apple" from the tuple, "apple" is the output of this print statement.
print(name)

