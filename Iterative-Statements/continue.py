for i in range(10):
    if i%2==0:
        continue
    print(i)
    
print()

cart = [13,26,500,630,5547,565,567,78,9,34355]
for item in cart:
    if item>500:
        print("We can't proceed with this item",item)
        continue
    print(item)
    
numbers = [10,20,0,49,60,23]
for n in numbers:
    if n==0:
        print("Hey, how we can divide with Zero.. Just skipping")
        continue
    print("100/{}={}".format(n,100/n))
    
print("*************")
cart1 = [10,2000,30,40,50]
for item1 in cart1:
    if item1 >= 500:
        print("We can not proceed this order")
    else:
        print("Congrats..")
        
        
x = 10
print(x)
del x


s = "Ashu"
print(s[0])
del s
#print(s)

r = "Ashu"
r = None
print(r)