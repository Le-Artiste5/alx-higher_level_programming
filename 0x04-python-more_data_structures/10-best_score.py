#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    retun = list(a_dictionary.keys())[0]
    bigger = a_dictionary[retun]
    for a, b in a_dictionary.items():
        if b > bigger:
            bigger = b
            retun = a
    return (retun)

