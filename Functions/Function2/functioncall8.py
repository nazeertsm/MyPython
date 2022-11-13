def test6(func) :
    def test7():
        func()
        print(func())
        print("this is my decorator functinon") 
        return func()
    return test7

def test8():
    return 5+ 7


print(test8() + 12)