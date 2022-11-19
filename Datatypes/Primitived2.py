num_char = len(input("what is your name?"))
#print("your name has" +num_char+ "characters.") #TypeError: can only concatenate str (not "int") to str
#-------string--------+integer+--string

#type checking
print(type(num_char))  #<class 'int'>

#type casting

new_num_char = str(num_char)
print("your name has " +new_num_char + " characters.")  #your name has 6 characters.

