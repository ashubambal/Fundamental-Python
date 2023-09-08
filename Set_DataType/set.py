s = {10,20,40,60}
print(s)
print(type(s))

l = [12,2,34,56,834,34,6,34]
l2 = l[::-1]
print(l2)

s = set(l)
print(s)
s.update(l2,range(5))
print(s)

p = {12,13,14,15,116,16,17,17,128}
print(p)
i= p.pop()
print(i)

p.discard(11)
print(p)