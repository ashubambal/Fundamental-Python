# * 
# * *
# * * *
# * * * *
# * * * * *

# First Way
# while True:
#     for j in range(int(input("Enter The no  for perimid :"))):
#         for i in range(j):
#             print("*",end=" ")
#         print()  

# Second Way
# n = int(input("Enter The No : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()      

# Third Way
n = int(input("Enter The No : "))
for i in range(1,n+1):
    print("*"*i)