n1 = int(input("Enter No 1: "))
n2 = int(input("Enter No 2: "))
n3 = int(input("Enter No 3: "))

if n1<n2 and n1<n3:
    print(f"{n1} is the smallest no as comapre to {n2},{n3}")
elif n2<n3:
    print(f"{n2} is the smallest no as comapre to {n1},{n3}")
else:
    print(f"{n3} is the smallest no as comapre to {n1},{n2}")