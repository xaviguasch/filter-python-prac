numbers = [0, -22, -13, 5, 7, 10, 2, -9]


def remove_negatives(num_list):
    return list(filter(lambda n: n >= 0, num_list))


print(remove_negatives(numbers))

