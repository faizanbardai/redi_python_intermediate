def is_sorted(list):
    for i in range(1, len(list)):
        current = list[i]
        previous = list[i - 1]
        if current < previous:
            return False
    return True


def find_not_sorted(list):
    for i in range(1, len(list)):
        current = list[i]
        previous = list[i-1]
        if current < previous:
            return current


def remove_not_sorted(list):
    sorted = [list[0]]
    for i in range(1, len(list)):
        current = list[i]
        previous = list[i-1]
        if current > previous:
            sorted.append(current)
    return sorted


def move_not_sorted(list):
    sorted_cars = [list[0]]
    unsorted_cars = []
    for i in range(1, len(list)):
        current = list[i]
        previous = list[i-1]
        if current > previous:
            sorted_cars.append(current)
        else:
            unsorted_cars.append(current)
    return [sorted_cars, unsorted_cars]


# 1. Write a function that returns true if a list is sorted.
fruits = ['apple', 'banana', 'cherry', 'lemon']
print(is_sorted(fruits))
# True

# 2. Write a function that returns the first element that is not in the ascending order.
numbers = [1, 2, 4, 3, 5]
print(find_not_sorted(numbers))
# 3

# 3. Write a function that remove all elements that are not in the ascending order.
print(remove_not_sorted(numbers))
# [1, 2, 4, 5]

# 4. Write a function that move the out of order elements to other list.
cars = ['audi', 'chevrolet', 'bmw', 'ford', 'honda', 'gmc']
sorted_cars, unsorted_cars = move_not_sorted(cars)
print(sorted_cars)
# ['audi', 'chevrolet', 'ford', 'honda']
print(unsorted_cars)
# ['bmw', 'gmc']
