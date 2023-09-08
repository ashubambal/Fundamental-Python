def sum_sub_mul_div(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a%b
    return sum,sub,mul,div

a = int(input("enter the 1st :"))
b = int(input("enter the 2nd : "))

t = sum_sub_mul_div(a,b)
print(t)
print(type(t))
for i in t:
    print(i)

x,y,z,p=sum_sub_mul_div(a,b)
print("The sum is :",x)
print("The Sub is :",y)
print("The Mul is :",z)
print("The div is :",p)