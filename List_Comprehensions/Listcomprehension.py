"""""""""""
List comprehension is a concise and efficient way to create lists in Python. 
It simplifies the process of generating lists by integrating a for loop, 
and optionally if conditions, into a single line of code. This approach
not only makes your code more readable but also often faster than using a traditional loop with list operations.

Basic Structure
A list comprehension consists of brackets containing an expression followed by a for clause, 
and then zero or more for or if clauses. The expression can be anything that results in a value, which forms part of the new list.

Syntax
The general syntax of a list comprehension is:
[new_expression for item in iterable if condition]

1. new_expression: This is the expression that defines how the elements of the new list are computed or transformed from the iterating variable item.
2. item: This is the variable representing each individual element from the iterable one at a time.
3. iterable: Any Python iterable (list, tuple, dict, set, etc.) which we want to iterate through.
4. condition (optional): A condition on the item that filters items from the iterable to be processed and included in the new list.
Example 1: Basic Usage
Let's say you want to create a list of the squares of numbers from 0 to 9.

"""""""""""
numbers = [1, 2, 3, 4, 5]
new_list = [x + 10 for x in numbers]
print(new_list)  # Output: [11, 12, 13, 14, 15]

#In this example, the expression x + 10 adds 10 to each element x in the numbers list,
#resulting in a new list new_list with the values [11, 12, 13, 14, 15].

print("------------------------")
#Example 2: Using an If Condition
#You can also include an if condition to filter elements from the iterable.
#For instance, let's create a list of squares of even numbers from 0 to 9.

numbers = [1, 2, 3, 4, 5]
new_list = [x ** 2 for x in numbers if x % 2 == 0]
print(new_list)  # Output: [4, 16]

#In this example, the list comprehension filters out odd numbers by checking if x % 2 == 0,
#and then squares the remaining even numbers to create a new list new_list with the values [4, 16].

print("------------------------")
#Example 3: Nested List Comprehension
#List comprehensions can also be nested within each other.
#For instance, let's create a list of tuples where each tuple contains a pair of numbers from two lists.

list1 = [1, 2, 3]
list2 = [10, 20, 30]
new_list = [(x, y) for x in list1 for y in list2]
print(new_list)  # Output: [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]

#In this example, the nested list comprehension iterates over each element x in list1 and each element y in list2,
#creating a tuple (x, y) for each pair of elements. The resulting new_list contains all possible combinations of pairs.
print("------------------------")

#Example 4: Using Enumerate in List Comprehension
#You can also use the enumerate() function within a list comprehension to get the index and value of elements.
#For instance, let's create a list of strings with their index values.

names = ['Alice', 'Bob', 'Charlie']
new_list = [f'{index}: {name}' for index, name in enumerate(names)]
print(new_list)  # Output: ['0: Alice', '1: Bob', '2: Charlie']
#In this example, the enumerate() function pairs each element name in the names list with its index,
#and the list comprehension creates a new list new_list with strings containing the index and name for each element.
print("------------------------")

squares = [x ** 2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#The above code creates a list of squares of numbers from 0 to 9 using a list comprehension.
#The expression x**2 computes the square of each number x, and the for x in range(10) iterates over the numbers 0 to 9.
print("------------------------")

#Example 5: Using a Conditional Expression
#You can include conditional expressions in list comprehensions to filter elements based on a condition.
#For instance, let's create a list of even numbers from 0 to 9.

numbers = [1, 2, 3, 4, 5]
new_list = [x for x in numbers if x % 2 == 0]
print(new_list)  # Output: [2, 4]

#In this example, the list comprehension filters out odd numbers by checking if x % 2 == 0,
#and includes only the even numbers in the new list new_list.
print("------------------------")

#Example 6: Using a Conditional Expression with If-Else
#You can also use conditional expressions with if-else statements in list comprehensions.
#For instance, let's create a list of 'even' or 'odd' strings based on the number parity.

numbers = [1, 2, 3, 4, 5]
new_list = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(new_list)  # Output: ['odd', 'even', 'odd', 'even', 'odd']

#In this example, the list comprehension checks if x % 2 == 0 to determine if the number is even or odd,
#and includes the corresponding string 'even' or 'odd' in the new list new_list.
print("------------------------")

#Example 7: Using Multiple Iterables
#You can use multiple iterables in a list comprehension to combine elements from different lists.
#For instance, let's create a list of tuples with elements from two lists.

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
new_list = [(x, y) for x in list1 for y in list2]
print(new_list)  # Output: [(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C'), (3, 'A'), (3, 'B'), (3, 'C')]
#In this example, the list comprehension pairs each element x in list1 with each element y in list2,
#creating a tuple (x, y) for each pair of elements. The resulting new_list contains all possible combinations of pairs.
print("------------------------")


#Example 8: Using a Function in List Comprehension
#You can also use functions within list comprehensions to transform or filter elements.
#For instance, let's create a list of squares of numbers using a custom function.

def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
new_list = [square(x) for x in numbers]
print(new_list)  # Output: [1, 4, 9, 16, 25]

#In this example, the square() function computes the square of a number x,
#and the list comprehension applies this function to each element in the numbers list to create a new list new_list.
print("------------------------")

#Example 9: Using a Nested List Comprehension
#You can nest list comprehensions within each other to create more complex structures.
#For instance, let's create a list of lists with elements from two lists.

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
new_list = [[x, y] for x in list1 for y in list2]
print(new_list)  # Output: [[1, 'A'], [1, 'B'], [1, 'C'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [3, 'C']]
#In this example, the nested list comprehension pairs each element x in list1 with each element y in list2,
#creating a list [x, y] for each pair of elements. The resulting new_list contains all possible combinations of lists.
print("------------------------")

#Example 10: Using a Conditional Expression with Multiple Iterables
#You can combine conditional expressions with multiple iterables in list comprehensions.
#For instance, let's create a list of tuples with elements from two lists based on a condition.

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
new_list = [(x, y) for x in list1 for y in list2 if x % 2 == 0]
print(new_list)  # Output: [(2, 'A'), (2, 'B'), (2, 'C')]
#In this example, the list comprehension pairs each element x in list1 with each element y in list2,
#but only includes the pairs where x % 2 == 0 (i.e., the even numbers) in the new list new_list.
print("------------------------")

#Example 11: Using a Conditional Expression with Nested List Comprehension
#You can combine conditional expressions with nested list comprehensions for more complex filtering.
#For instance, let's create a list of lists with elements from two lists based on a condition.

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']
new_list = [[x, y] for x in list1 for y in list2 if x % 2 == 0]
print(new_list)  # Output: [[2, 'A'], [2, 'B'], [2, 'C']]
#In this example, the nested list comprehension pairs each element x in list1 with each element y in list2,
#but only includes the pairs where x % 2 == 0 (i.e., the even numbers) in the new list new_list.
print("------------------------")

#Example 12: Using a Conditional Expression with If-Else in Nested List Comprehension
#You can also use conditional expressions with if-else statements in nested list comprehensions.
#For instance, let's create a list of 'even' or 'odd' strings based on the number parity in a nested list.

numbers = [1, 2, 3, 4, 5]
new_list = ['even' if x % 2 == 0 else 'odd' for x in numbers]
nested_list = [[x, y] for x in new_list for y in numbers]
print(nested_list)
# Output: [['odd', 1], ['odd', 2], ['odd', 3], ['odd', 4], ['odd', 5], ['even', 1], ['even', 2], ['even', 3], ['even', 4], ['even', 5]]
#In this example, the nested list comprehension pairs each element x in new_list with each element y in numbers,
#creating a list [x, y] for each pair of elements. The resulting nested_list contains all possible combinations of lists.
print("------------------------")

#Example 13: Using a Conditional Expression with If-Else in Nested List Comprehension
#You can also use conditional expressions with if-else statements in nested list comprehensions.
#For instance, let's create a list of 'even' or 'odd' strings based on the number parity in a nested list.

numbers = [1, 2, 3, 4, 5]
new_list = ['even' if x % 2 == 0 else 'odd' for x in numbers]
nested_list = [[x, y] for x in new_list for y in numbers]
print(nested_list)
# Output: [['odd', 1], ['odd', 2], ['odd', 3], ['odd', 4], ['odd', 5], ['even', 1], ['even', 2], ['even', 3], ['even', 4], ['even', 5]]
#In this example, the nested list comprehension pairs each element x in new_list with each element y in numbers,
#creating a list [x, y] for each pair of elements. The resulting nested_list contains all possible combinations of lists.
