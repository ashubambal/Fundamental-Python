s = {12,23,344,565,12,"Ashu"}
print(type(s))

f = frozenset(s)
print(f)
for i in f:
    print(i)
s.add(12)
