# x = firstvalue if condition else secondvaue

a,b = 10,20
x=30 if a>b else 40
print(x)

# x = int(input("Enter The first no:"))
# y = int(input("Enter The second no:"))
# min = x if x<b else y
# print("Min Value :", min)


x = int(input("Enter The first no:"))
y = int(input("Enter The second no:"))
z = int(input("Enter The third no:"))
min = x if x<y and x<z else y if y<z else z
print("Min Value :", min)

l = int(input("Enter The First NO: "))
m = int(input("Enter The Second No: "))
n = int(input("Enter The Third No: "))

max = l if l>m and l>n else m if m>n else n 
print(max)