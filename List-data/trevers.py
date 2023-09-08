l = [1,2,34,5,6,7,8,9,0,1,0,2,3,4,1,0,1,3,1,4,14,]
l2 = []
i = 0
while i<len(l):
    print(l[i])
    i=i+1
    
for x in l:
    if x%2==0:
        print("Even No : ", x)
        
l1 = ["A","B","C","D"]
x = len(l1)
print(x)
for i in range(x):
    print("+ve = {}, -ve = {} , Item = {}".format(i,i-x,l[i]))
    
# Important function about list
print(len(l1))
print(l.count(0))
print(l2.append(l.count(0)))

l1.append("E")
print(l1)
l1.insert(2,234)
print(l1)

lx = []
for x in range(101):
    if x%10==0:
        lx.append(x)
print(lx)

lx.extend(l1)
print(lx)

Math_Stud = ["Ashu","Ram","Gopi","Rahul"]
Sci_Stud = ["Rahul","Naveen","Shyam","Ravi"]

Math_Stud.extend(Sci_Stud)
print(Math_Stud)
x = input("Enter Name : ")

Math_Stud.remove(x)
print(Math_Stud)
if x in Math_Stud:
    print("{} entry is duplicate on list hence removing : ".format(x))
else:
    print("{} is not duplicate entry on the list".format(x))

print(Math_Stud)
print(Math_Stud.pop())


