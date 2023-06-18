#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = sum(map(lambda x: x[0] * x[1], my_list))
    denominator = sum(map(lambda y: y[1], my_list))

    if denominator != 0:
        result = numerator / denominator
        return result
    else:
        return 0
