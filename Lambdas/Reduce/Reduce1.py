from functools import reduce


l= [1, 2, 3, 4, 5, 6, 7, 8]


l1 = [3]

print(reduce(lambda a,b : a *b , l1))  #3



#reduce(lambda a,b : a *b ,5)

""""
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [97], in <cell line: 1>()
----> 1 reduce(lambda a,b : a *b ,5)

TypeError: reduce() arg 2 must support iteration

"""