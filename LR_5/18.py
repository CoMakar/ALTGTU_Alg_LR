import random as rnd
import lib.list_functions as lfunc
import lib.math_functions as mfunc


def count_smaller_than_c(arr: list, c: int):
    counter = 0

    for elem in arr:
        counter += 1 if elem < c else 0
        
    return counter


def sum_of_integers_after_min(arr: list):
    sum_val = 0

    reversd_arr = lfunc.reverse(arr)
    min_index = lfunc.min_index(reversd_arr)

    for c in range(min_index):
        sum_val += int(reversd_arr[c])
        
    return sum_val


def sort_per_20(arr: list):
    max_val = lfunc.max(arr)
    per_20 = []
    others = []
    
    for c in range(len(arr)):
        if mfunc.abs(max_val - arr[c]) / max_val < 0.2:
            per_20.append(arr[c])
        else:
            others.append(arr[c])

    return per_20 + others


def main():
    n = int(input("Enter the amount of numbers [n value]: "))
    c = int(input("Enter the C: "))

    if n <= 0:
        print("n value must be greater than 0")
        return

    arr = [round(rnd.uniform(-100, 100), 2) for i in range(n)]

    print("[")
    for elem in arr:
        print("    ", elem, sep="")
    print("]")

    print("Amount of elements smaller than C:", count_smaller_than_c(arr, c))
    print("Max", lfunc.max(arr), "at", lfunc.max_index(arr))
    print("Min", lfunc.min(arr), "at", lfunc.min_index(arr))
    print("Sum of integer parts of elements after min:", sum_of_integers_after_min(arr))
    print("20% Similarity first:", sort_per_20(arr))


if __name__ == "__main__":
    main()