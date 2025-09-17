def new_in_list(my_list, idx, element):
    if (idx < 1) or (idx > len(my_list) -1):
        return my_list
    else:
        copy = [x for x in my_list]
        copy[idx] = element
        return copy