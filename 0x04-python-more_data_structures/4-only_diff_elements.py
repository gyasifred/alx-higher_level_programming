#!/usr/bin/python
def only_diff_elements(set_1, set_2):
    return [i for i in set_1 | set_2 if i not in set_1.intersection(set_2)]
