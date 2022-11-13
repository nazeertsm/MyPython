l = [1,2,3,4,5,6,7,8]

def test24(a):
    l = []
    if type(a) == list :
        for i in a :
            if i%2 == 0 :
                l.append(i)
    return l

print(test24(l))  #[2, 4, 6, 8]