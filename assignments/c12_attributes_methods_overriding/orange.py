# 1. Create an Orange class that has one class variable named “count” used
#    to track to track the number of oranges in existence.
# 2. All oranges should have a “weight” instance variable.
# 3. Create 3 different oranges. Make sure your “count” class variable tracks
#    the count correctly.
# 4. Create a separate function (not bound to a class) to add the weight of
#    each orange and get the result.
# 5. Can you think of a way to also track the weight as a class variable?


class Orange:
    count = 0  # class variable
    weight = 0  # weight can also be tracked like this

    def __init__(self, weight):
        Orange.count += 1
        Orange.weight += weight

        # 2. All oranges should have a “weight” instance variable.
        self.weight = weight  # instance variable

# A separate function (not bound to a class) to add the weight of
# each orange and get the result.


def calculate_weight(oranges):
    weight_of_all_oranges = 0
    for orange in oranges:
        weight_of_all_oranges += orange.weight
    return weight_of_all_oranges


if __name__ == '__main__':
    # 3. Create 3 different oranges. Make sure your “count” class variable tracks
    #    the count correctly.
    orange1 = Orange(10)
    print(Orange.count, orange1.weight, Orange.weight)
    orange2 = Orange(20)
    print(Orange.count, orange2.weight, Orange.weight)
    orange3 = Orange(30)
    print(Orange.count, orange3.weight, Orange.weight)

    total_weight = calculate_weight([orange1, orange2, orange3])
    print(total_weight)
    print(Orange.weight)
