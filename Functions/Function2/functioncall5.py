def test1(func) : 
    def test2():
        print("i am inside test2 " ) 
        func()
        print(func())
        
        print("functino executed ")
        return func()
    return test2 

@test1
def test4():
    return 5+6



print(test4() + 56)