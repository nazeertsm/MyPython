def test5(*args):
    l = []
    for i in args:
        l.append(i)
    return l

s= test5(34,56,23,87)

print(s)

