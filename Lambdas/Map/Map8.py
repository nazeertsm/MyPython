l = [1,2,3,4,5,6,7,8]

a = lambda a :a if  a %2 == 0 else None 


print(list(map(a , l)))  #[None, 2, None, 4, None, 6, None, 8]


print(list(filter(a , l)))  #[2, 4, 6, 8]


def test25(a):
    if a%2 ==0 :
        return False  
    else :
        return True 


print(test25(32))  #False

print(test25(35))  #True

print(list(filter(test25,l)))  #[1, 3, 5, 7]

print(sum(l))   #36