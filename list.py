l = [10,20,"ASHU","yes",True,34.9,10,10]
l.append("Bambal")
l.remove("ASHU")
print(l)


l1 = ["Ashutosh",True,10,20.8,10+2j]
print(l1)
print(type(l1))
for items in l1:
    print(items)
l1.append(200)
print(l1)
l1[2]="Bambal"
print(l1)
l1.remove(20.8)
print(l1)

print(l1[-1])
print(l1[0:4])
l3 = l1*2
print(l3)
l1.remove(l1[-2])
print(l1)