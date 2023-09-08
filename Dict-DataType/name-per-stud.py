# rec = {}
# n = int(input("Enter The no of Students:"))
# i = 1
# while i<=n:
#     name = input("Enter Student name : ")
#     marks = int(input("Enter The Student Marks : "))
#     rec[name] = marks
#     i = i+1
# print("Name of Student","\t","% of marks")
# for x in rec:
#     print("\t",x,"\t\t",rec[x])

dict = {1:"A",2:"B",3:"C"}
print(dict.get(3))
#print(d)
print(dict)
dict[4]="D"
print(dict)
dict[1]="Z"
print(dict)
del dict[1]
print(dict)
dict.clear()
print(dict)



print("********************************")

dt = {1:"A",2:"B",3:"C"}

for k,v in dt.items():
    print(k,"--",v)

ke = dt.keys()
va = dt.values()
print(ke)
print(va)
for v in dt.values():
    print(v)

for k in dt.keys():
    print(k)





print(dt.pop(2))
print(dt)

print(dt.popitem())
print(dt)