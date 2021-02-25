import math


def center_zeros(a_list):
    center = math.floor(len(a_list) / 2)
    new_list = a_list.copy()
    for i in new_list:
        if i in new_list == 0:
            new_list.pop(i)
            new_list.insert(i, center)
        return new_list


center_zeros([1, 1, 3, 0, 6, 0])
center_zeros([0, 3, 1])
center_zeros([1, 1, 3, 0])
