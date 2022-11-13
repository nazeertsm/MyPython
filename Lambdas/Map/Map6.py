l = [1,2,3,4,5,6,7,8]

l1 = []
for i in l :
    if i % 2 == 0 :
        l1.append(i)



print([i for i in l if i%2 == 0 ])  #[2, 4, 6, 8]