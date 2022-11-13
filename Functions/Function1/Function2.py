""""
Example: Python *args
 *args parameter lets the function accept any number of arguments. 
In this example, we will write an addition function that can accept any number of arguments 
and returns the addition of all these arguments. """


def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

sum1= addition(2)
sum2= addition(2,3)
sum3= addition(2,3,4)

print(sum1)
print(sum2)
print(sum3)


def test3(*args) : 
    return args

print(type(test3(1,2,3,4,"sudh"))) #<class 'tuple'>



def test4(*args):
    return list(args)

print(test4("sudh" , True , 8+7j , 34, 34.56))  #['sudh', True, (8+7j), 34, 34.56]