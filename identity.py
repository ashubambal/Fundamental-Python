a=10
b=10
print(id(a))
print(id(b))
print(a is b)

x = "Ashu"
y = "Ashu"
print(id(x))
print(id(y))
print(x is y)

list1 = ["Ashu",10,20]
list2 = ["Ashu",10,10]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)