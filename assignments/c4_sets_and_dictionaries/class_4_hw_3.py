# Create a new dictionary called „people“ and add a new entry with your name as key and phone number as value
# [dictionary should contain at least 5 keys]
people = {
    'faizan': '123',
    'faizan1': '123',
    'faizan2': '123',
    'faizan3': '123',
    'faizan4': '123'
}

# WAP to print all dictionary value in the given format :
# if your dictionary looks like this →{'sameer': 123, 'sameer1': 123, 'sameer2': 123, 'sameer3': 123, 'sameer4': 123}
for x, y in people.items():
    print('The phone number of', x, 'is', y)

# WAP to ask name to user if exists in the dictionary output the phone number.
# If doesn't exist in dictionary output “The user doesn’t exist”
while True:
    name = input('Name please: ')
    if name in people:
        print(people[name])
    else:
        print('The user doesn\'t exist')
