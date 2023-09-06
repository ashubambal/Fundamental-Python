a = [10,20,30,40,255]
b = bytes(a)
print(type(b))
print(id(b))
a[0]=100
print(a)
# b[0]=100
# print(b)
for i in b:
    print(i*2)
    print(type(b))