# Find the index of the first occurrence of a substring in a string.
# So given the word “The worlds fastest plane”, find the substring “plane” and “car” and print
# the output.

string = 'The worlds fastest plane'
to_test = ['plane', 'car']

for i in to_test:
    print(i, string.find(i))
    print(i in string)
