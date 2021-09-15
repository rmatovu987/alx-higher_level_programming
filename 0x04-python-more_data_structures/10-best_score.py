#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    sort_dict = sorted(a_dictionary, key=lambda x: a_dictionary[x])
    return sort_dict[-1]
