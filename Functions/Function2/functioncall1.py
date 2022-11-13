def test1(func) : 
    def test2():
        print("i am inside test2 " ) 
        func()
        print(func())
        
        print("functino executed ")
        return func()
    return test2 

@test1
def test3():
    print("this is my test3")


print(test3())

print(test1(test3()))