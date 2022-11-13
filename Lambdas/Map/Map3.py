l = ["sudh" , "kumar" , "ineuron"]

l1 = []
for i in l :
    l1.append(i.upper())


print(l1) #['SUDH', 'KUMAR', 'INEURON']

print(list(map(lambda a : a.upper(), l)))  #['SUDH', 'KUMAR', 'INEURON']

print(list(map(str.upper , l)))  #['SUDH', 'KUMAR', 'INEURON']