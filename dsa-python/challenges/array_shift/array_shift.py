from math import ceil
arr = [2, 4, 6, 8]
n = int(input('insert number: '))


def insert_shift_array(lst, val):
    mid = int(ceil(len(lst) / 2))
    new_arr = lst[:mid] + [val] + lst[mid:]
    print(new_arr)


insert_shift_array(arr, n)
