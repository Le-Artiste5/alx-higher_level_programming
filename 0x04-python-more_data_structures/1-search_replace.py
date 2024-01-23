#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            replaced.append(replace)
        else:
            replaced.append(my_list[i])
    return replaced
