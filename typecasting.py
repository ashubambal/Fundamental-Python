print(int(1234.56565))
print(int(True))
print(int("100"))

a = "1"
print(int(a))
print(float(a))
print(complex(a))
print(bool(a))
str(a)


x = 10
y = 10
print(x is y)
print(id(x))
print(id(y))

x1 = 10+5j
y1 = 10+5j
print(x1 is y1)
print(id(x1))
print(id(y1))

x2 = 10.0
y2 = 10.0
print(x2 is y2)
print(id(x2))
print(id(y2))

x3 = 10
y3 = 10
print(x3 is y3)
print(id(x3))
print(id(y3))

x = 'durga'
y = 'durga'
print(x is y)
print(id(x))
print(id(y))