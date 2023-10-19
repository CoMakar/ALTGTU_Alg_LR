import random as rnd
import lib.list_functions as lfunc


def sum_of_negatives(arr: list):
    sum_val = 0

    for elem in arr:
        sum_val = sum_val + elem if elem < 0 else sum_val

    return sum_val


def production_of_inbetweens(arr: list):
    production = 1

    index_0 = lfunc.max_index(arr)
    index_1 = lfunc.min_index(arr)

    start = (index_0 if index_0 < index_1 else index_1) + 1
    stop = index_1 if index_1 > index_0 else index_0

    for c in range(start, stop):
        production *= arr[c]

    return production


def main():
    n = int(input("Enter the amount of numbers [n value]: "))
    
    if n <= 0:
        print("n value must be greater than 0")
        return
    
    arr = [round(rnd.uniform(-100, 100), 2) for i in range(n)]

    print("[")
    for elem in arr:
        print("    ", elem, sep="")
    print("]")
    
    print("Sum of negatives:", sum_of_negatives(arr))
    print("Max", lfunc.max(arr), "at", lfunc.max_index(arr))
    print("Min", lfunc.min(arr), "at", lfunc.min_index(arr))
    print("Production of inbetweens:", production_of_inbetweens(arr))
    print("Sorted array: ", lfunc.qsort(arr))


if __name__ == "__main__":
    main()