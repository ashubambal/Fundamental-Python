l = [10,0,23,34,2,456,85,23,56]
l1 = [10101,2022,232,32]
print(l+l1)
print(l*5)
print(l+["A"])
l.sort()
print(l)
l.reverse()
print(l)


l2 = [10,20,30,[40,50,[60,70]]]
print(l2[0])
print(l2[3][2][1])


l3 = [[1,2,3],[4,5,6],[7,8,9]]
# i = len(l3)
for i in l3:
    print(i)
    
l4 = [x*x for x in range(1,11)]
l5 = [x**2 for x in range(1,6)]
l6 = [x for x in l4 if x%2==0]
print(l4)
print(l5)
print(l6)

words = ["Ram","Shyam","Hemant","Ramesh"]
l = [w[0] for w in words]
print(l)


num1 = [10,20,30,40]
num2 = [30,40,50,60]

num3 = [i for i in num1 if i not in num2]
print(num3)

ls = [10,23,2,6,23,67,23,787,12]

ls.sort()
print(ls)
sl = [len(ls) for w in ls]
print(sl)






