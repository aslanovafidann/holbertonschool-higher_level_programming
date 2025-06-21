#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_value = float('-inf')
    for k, v in a_dictionary.items():
        if v > best_value:
            best_value = v
            best_key = k
    return best_key
