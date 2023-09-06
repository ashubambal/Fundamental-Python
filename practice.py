# a = 23
# b = 30

# print("Result is :",(a+b))

# a = int(input("Enter the first no: "))
# b = int(input("Enter The Second no: "))

# result = a+b
# print(result)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b   
 
def mul(a,b):
    return a*b  

def div(a,b):
    return a/b

print('''Which Operation you want to perform
      1. add
      2. sub
      3. mul
      4. div
      ''')
operation = int(input("Enter the no that the operation you want to perform: "))
if operation == 1:
    print("You have selecetd addition operation")
    a = int(input("Enter the first no: "))
    b = int(input("Enter The Second no: "))
    result = add(a,b)
    print(f"Addition of {a} and {b} is:",result)
elif operation == 2:
    print("You have selecetd substartction operation")
    a = int(input("Enter the first no: "))
    b = int(input("Enter The Second no: "))
    result = sub(a,b)
    print(f"substartction of {a} and {b} is:",result)
elif operation == 3:
    print("You have selecetd multiplication operation")
    a = int(input("Enter the first no: "))
    b = int(input("Enter The Second no: "))
    result = mul(a,b)
    print(f"multiplication of {a} and {b} is:",result)
elif operation == 4:
    print("You have selecetd division operation")
    a = int(input("Enter the first no: "))
    b = int(input("Enter The Second no: "))
    result = div(a,b)
    print(f"division of {a} and {b} is:",result)
else:
    print("You have selected unknown option, please select correct one")