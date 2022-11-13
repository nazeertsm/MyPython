def test6(func) :
    def test7():
        func()
        print(func())
        print("this is my decorator functinon") 
        return func()
    return test7

@test6
def test8():
    return 5+ 7


print(test8())

print(test8() + 100)

print(type(test8()))