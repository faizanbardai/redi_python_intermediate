def multiply_with_allergy(x, y):
    if x == 42 or y == 42:
        raise ValueError("Sorry, I'm allergic to 42")
    else:
        result = x*y
        return result


def square(x):
    try:
        return multiply_with_allergy(x, x)
    except ValueError:
        return x*x


number_as_str = input("Enter a number to square: ")
number = int(number_as_str)

# TODO: try to square (also in case of 42)
result = square(number)
# TODO: except if a ValueError occurs, then square "manually" using result=x*x
print(f"The square is: {result}")
