# copy these sets into new *.py file
set_1 = {"A", "B", "E", "J", "L", "O", "K", "Y", "N"}
set_2 = {"c", "B", "D", "N", "P", "Y", "A", "J", "M"}

# print common elements in both sets
print(set_1.intersection(set_2))

# print total number of number unique alphabets from both sets
print(len(set_1.union(set_2)))

# print alphabets that are in set2 but not in set1
print(set_2.difference(set_1))
