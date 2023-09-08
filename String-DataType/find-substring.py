# s = "Learning Python Is very easy"
# print(s.find("I"))
# print(s.rfind("I"))
# print(s.index("P"))
# print(s.find("y",1,-1))

# string = input("Enter the main string : ")
# sub = input("Enter the substring : ")

# try:
#     n=s.index(sub)
# except:
#     print("Substring not found")
# else:
#     print("Substring found")

s = input("Enter The main string : ")
sub = input("Enter The sub string : ")
pos = -1
n = len(s)
flag = False
while True:
    pos = s.find(sub,pos+1,n)
    if pos==-1:
        break
    print("found at Position :",pos)
    flag=True
if flag == False:
    print("Not Fuound")