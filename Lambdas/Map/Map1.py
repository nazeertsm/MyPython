l = [1,2,3,4,5,6,7]
l1  = [] 
for i in l :
    l1.append(i+10) #[11, 12, 13, 14, 15, 16, 17]

print(l1)


def test14(a):
    return a + 10


print(list(map( test14,l ))) #[11, 12, 13, 14, 15, 16, 17]




print(list(map(lambda a : a +10  , l)))  #[11, 12, 13, 14, 15, 16, 17]