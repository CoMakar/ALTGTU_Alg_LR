import random as rnd
import lib.list_functions as lfunc


def sum_of_inbetweens(arr: list):
    sum_val = 0
    index_0 = -1
    index_1 = -1

    for c in range(len(arr)):
        if arr[c] > 0 and index_0 == -1:
            index_0 = c
        
        if arr[c] > 0 and index_0 != -1:
            index_1 = c
        
    start = (index_0 if index_0 < index_1 else index_1) + 1
    stop = index_1 if index_1 > index_0 else index_0

    for c in range(start, stop):
        sum_val += arr[c]

    return sum_val


def zero_first_sort(arr: list):
    zeros = [i for i in arr if i == 0]
    not_zeros = [i for i in arr if i != 0]

    return zeros + not_zeros


def main():
    n = int(input("Enter the amount of numbers [n value]: "))
    zeros_amount = rnd.randint(-1, n // 2) + 1
    
    if n <= 0:
        print("n value must be greater than 0")
        return
    
    arr = [round(rnd.uniform(-100, 100), 2) for i in range(n)]
    
    for i in range(zeros_amount):
        arr[rnd.randint(0, n - 1)] = 0

    print("[")
    for elem in arr:
        print("    ", elem, sep="")
    print("]")
    
    print("Min", lfunc.min(arr), "at", lfunc.min_index(arr))
    print("Sum of inbetweens", sum_of_inbetweens(arr))
    print("Zeros first sorted array:", zero_first_sort(arr))


if __name__ == "__main__":
    main()