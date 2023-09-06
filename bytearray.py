a = [10,20,30,240,255]
print(type(a))
a[0] = 100
print(a)
b = bytearray(a)
print(type(b))
b[0] = 2
print(b)