n = {"A":100,"B":300,"C":500}
s = sum(n.values())
print("Sum = ",s)

word = "Ashutosh Bambal Kanfodi"
d = {}
for x in word:
    d[x] = d.get(x,0)+1
    print(x)
for k,v in d.items():
    print(k,"occured",v,"times")