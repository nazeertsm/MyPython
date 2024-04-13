"""""""""
The enumerate() function
 is another built-in Python function that allows you to iterate over a sequence while keeping track 
of each element’s index. Similar to zip(), 
it returns an iterator that produces pairs of indices and elements. Here’s an example:
"""""""""
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
   print(index, letter)

print("------------------------")

"""""""""
Note that the default starting index is zero, but you can assign it
to whatever you want when you call the enumerate() function. For example:
"""""""""
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, 2):
   print(index, letter)

print("------------------------")

# enumerate() is particularly useful when you need both the index and the element in a loop.
# For instance, you can use it to iterate over a list and update the elements at the same time:
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
   letters[index] = f'{letter}-{index}'
print(letters)
# Output: ['a-0', 'b-1', 'c-2']

print("------------------------")

# You can also use enumerate() to create a dictionary that maps elements to their indices:
letters = ['a', 'b', 'c']
indexed_letters = {index: letter for index, letter in enumerate(letters)}
print(indexed_letters)
# Output: {0: 'a', 1: 'b', 2: 'c'}








