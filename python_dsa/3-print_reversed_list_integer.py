# def print_reversed_list_integer(my_list=[]):
#     for num in range(len(my_list) -1, -1, -1):
#         print('{:d}'.format(my_list[num]))



def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print('{:d}'.format(num))