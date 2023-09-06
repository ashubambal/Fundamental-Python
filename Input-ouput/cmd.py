from sys import argv
# print("The Number of command line arguments : ",len(argv))
# print("The list of command line argv ",argv)
# print("Print command line argv one by one ")
# for x in argv:
#     print(x)

sum =0 
args = argv[1:]
for x in args:
    n = int(x)
    sum = sum+n
print("The Sum:",sum)