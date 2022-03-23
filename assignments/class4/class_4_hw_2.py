# Copy the below lines into *.py file
new_dict = {"name": "xyz", "age": 0}

print("Previous :", new_dict)

# Write your code here
new_dict["name"] = input('Enter your name: ')
new_dict["age"] = int(input('Enter your age: '))

print("After Update:", new_dict)
