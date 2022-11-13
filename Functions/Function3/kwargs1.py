def test6(func) :
    def test7(*args,**kwargs):
        func(*args,**kwargs)
        print(func(*args,**kwargs))
        print("this is my decorator functinon") 
        return func(*args,**kwargs)
    return test7


@test6
def test8(a,b):
    return a+b


print(test8("sudh" , "kumar"))
