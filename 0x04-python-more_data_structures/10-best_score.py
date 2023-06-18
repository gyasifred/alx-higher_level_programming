#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    max_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_key
