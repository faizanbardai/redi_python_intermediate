# 1. Create a function that takes an integer x as input and returns a list of first x
# Fibonacci numbers
# 2. In your python script:
# ○ Ask the user how many Fibonacci numbers he wants to see, store the result in
# a variable called x
# ○ Create a text file called Fibonaccis.txt which contains the first x Fibonacci
# numbers in ascending order
# Hint: Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13, …

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'Fibonaccis.txt'


def get_Fibonacci_series(limit):
    # Using dictionary to memoize function
    Fibonacci = {}

    def get_Fibonacci_by(limit):
        # checking in dictionary if the key exists and returning value (Memoization)
        if limit in Fibonacci:
            return Fibonacci[limit]

        # Constant value for limit 1 and 2
        if limit == 1:
            Fibonacci[1] = 1
            return Fibonacci[limit]
        if limit == 2:
            Fibonacci[1] = 1
            Fibonacci[2] = 1
            return Fibonacci[limit]

        # else calculating the one-down and two-down value recursively
        n1 = get_Fibonacci_by(limit - 1)
        n2 = get_Fibonacci_by(limit - 2)

        # Assigning the value to key
        Fibonacci[limit] = n1 + n2

        # Returning the sum
        return Fibonacci[limit]

    get_Fibonacci_by(limit)

    with open(path, 'w') as file:
        file.write(", ".join([str(x) for x in Fibonacci.values()]))


limit = int(input('How many Fibonacci numbers you want? '))
get_Fibonacci_series(limit)
