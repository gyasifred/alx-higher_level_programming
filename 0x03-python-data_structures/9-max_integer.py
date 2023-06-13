#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    max_num = my_list[0]
    for num in my_list:
        if num > my_list:
            max_num = num
        else:
            continue
    return max_num
