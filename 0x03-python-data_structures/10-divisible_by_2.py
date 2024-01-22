#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lent = len(my_list)
    n_list = []
    for i in range(lent):
        if my_list[i] % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return n_list
