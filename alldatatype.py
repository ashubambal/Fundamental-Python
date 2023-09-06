l = [10,20]
l.append("Ashu")
print(l)
l.remove(10)
print(l)

s = {10,20}
s.add("Ashu")
print(s)
s.remove(10)
print(s)

my_dict = {1: '10', 2: '20', 3: 'Ashu'}
value_to_remove = '10'

# Create a copy of the dictionary to avoid modifying it during iteration
copy_dict = my_dict.copy()

for key, value in copy_dict.items():
    if value == value_to_remove:
        del my_dict[key]

print(my_dict)