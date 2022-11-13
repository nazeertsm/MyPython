l = ["sudh" , "kumar" , "ineuron"]

def upper_string(a) : 
    return a.upper()


print(list(map(upper_string, l)))  #['SUDH', 'KUMAR', 'INEURON']

print(l)  #['sudh', 'kumar', 'ineuron']

print(list(map(len,l)))  #[4, 5, 7]

print(list(map(lambda a : len(a) , l)))  #[4, 5, 7]