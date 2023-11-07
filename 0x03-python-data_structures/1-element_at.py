#!/usr/bin/python3
def element_at(my_list, idx):
    listlength = len(my_list) - 1
    if (idx < 0 or idx >= len(my_list)):
        return (None)
    else:
        return (my_list[idx])
