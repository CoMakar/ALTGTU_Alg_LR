def reverse(arr: list):
    reversed_arr = []

    for c in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[c])

    return reversed_arr


def max(arr: list):
    max_val = arr[0]

    for elem in arr:
        max_val = elem if elem > max_val else max_val

    return max_val


def min(arr: list):
    min_val = arr[0]

    for elem in arr:
        min_val = elem if elem < min_val else min_val

    return min_val


def max_index(arr: list):
    index = 0
    max_val = arr[0]

    for c in range(len(arr)):
        if arr[c] > max_val:
            index = c
            max_val = arr[c]

    return index


def min_index(arr: list):
    index = 0
    min_val = arr[0]

    for c in range(len(arr)):
        if arr[c] < min_val:
            index = c
            min_val = arr[c]

    return index


def qsort(arr: list):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    pivot = arr[len(arr) // 2]

    lower = qsort([el for el in arr if el < pivot])
    equal = [el for el in arr if el == pivot]
    higher = qsort([el for el in arr if el > pivot])

    return lower + equal + higher


def insort(arr: list, sort_logic=lambda x, y: x > y):
    arr_sort = [elem for elem in arr]
    
    for i in range(1, len(arr_sort)):
        j = i
        while j > 0 and sort_logic(arr_sort[j - 1], arr_sort[j]) :
            arr_sort[j - 1], arr_sort[j] = arr_sort[j], arr_sort[j - 1]
            j -= 1
            
    return arr_sort
