# name = input("Enter your name : ")
# if name == "Ashu":
#     print(f"Hello {name}, how are you")
# else:
#     print(f"Hello Guest, How are you doing !!")

n1 = int(input("Enter the first no : "))
n2 = int(input("Enter the second no : "))
n3 = int(input("Enter the third no : "))

if n1>n2 and n1>n3:
    print(f"{n1} is greater than {n2} and {n3}")
elif n2>n3:
    print(f"{n2} is greater than {n1} and {n3}")
else:
    print(f"{n3} is greater than {n1} and {n2}")
    