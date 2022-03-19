user_number = int(input('Enter Number: '))
accumulator = 0

for i in range(1, user_number + 1):
    accumulator += i

print('Sum is ', accumulator)
