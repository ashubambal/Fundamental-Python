# 1 = 1
# 2 = 1*2
# 3 = 1*2*3
#
# 5 = 1*2*3*4*5 = 120


def fact(num):
    result = 1
    while num>=1:
        result = result*num # 1*3 =3, 2*3=6
        num = num-1
    return result

num = int(input("Enter the no : "))
print(fact(num))    