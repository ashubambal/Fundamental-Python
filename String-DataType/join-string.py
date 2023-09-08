tuple = ("Ashutosh","Ram","Gopal","Ankush")
j = '-'.join(tuple)
print(j)

l = ["Pune","Mumbai","Goa","Delhi"]
j = ".".join(l)
print(j)

s = "Bhai Kya Kar raha hai tu"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print(s.startswith("B"))
print(s.endswith("u"))

s1 ="ashutoshabmbal010298"
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
print(s1.islower())
print(s1.isupper())
print(s1.isspace())




str = input("Enter any string : ")
if str.isalnum():
    print("Alpha Nmeric Charector")
    if str.isalpha():
        print("Alphabet character")
        if str.islower():
            print("Lower case alphabet charector")
        else:
            print("Upper case alphabet charector")
    else:
        print("It is digit")
elif str.isspace:
    print("It is spcae charector")
else:
    print("Non Space charector")