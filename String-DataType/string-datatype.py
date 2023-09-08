# s = "Ashutosh Bambal"
# for item in s:
#     print(item)
# print()

# print(s[0])
# s1 = "Ashutosh Bambal"
# for slice in s1[2:5]:
#     print(slice)

s = input("Enter String :")
i = 0
for x in s:
    print("The +ve {} index and -v {} index for {}".format(i,i-len(s),x))
    i=i+1