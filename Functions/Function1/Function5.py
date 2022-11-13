def test26(a : int ,b : "func", c:int  = 234) -> int:
    '''this is my doc string to give a hint to next programer '''
    return a +b +str(c)


print(test26("sudh"  , "kumar" , 345))  #sudhkumar345