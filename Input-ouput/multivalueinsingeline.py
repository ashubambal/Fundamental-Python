# a,b = [int(x) for x in input("Enter two numbers : ").split(",")]
# print("Product is :" ,a*b)


# a,b = [int(x) for x in input("Enter two no :").split(",")]
# print("Product is : ",a*b)

url = "https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Home:"
u = url.split("/")
print(type(u))
for each in u:
    print(each)
    
a,b,c = [int(x) for 
         x in input("Enter The no : ").split()]
print("Sum : ",a+b+c)