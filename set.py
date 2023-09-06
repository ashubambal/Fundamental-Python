l = {10,20,"ASHU","yes",True,34.9,10,10}
l = {10}
print(type(l))
print(l)

l.add("BAAAAAAAAAAAA")
l.add(10000)
print(l)


s = {10,20,20,30,"Ashu"}
print(type(s))
print(s)
s.add(12)
print(s)
s.remove(s[0])
print(s)