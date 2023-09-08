# s = "Ashutosh Bambal"
# l = len(s)
# print(l)
# print("Forword Direction : ")
# i = 0
# while i<l:
#     print(s[i],end="")
#     i+=1
# print("Backword Direction:")
# i = -1
# while i>-l:
#     print(s[i],end="")
#     i=i-1

s = "Ashutosh Bambal"
print("Forword Direction 2: ")
for i in s:
    print(i,end=" ")

for i in s[::]:
    print(i,end=" ")

for i in s[::-1]:
    print(i,end=" ")
    
    
print("***********************")

print("A" in s)
print("A" not in s)

string = input("Enter The String : ")
sub = input("Enter The Sub String : ")
if sub in string:
    print(sub,"substring available on main string")
else:
    print(sub,"substring is not available on maion string")