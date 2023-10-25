import random as rnd
import lib.list_functions as lfunc


def sum_of_positives_before_max(arr: list):
    sum_val = 0

    max_index = lfunc.max_index(arr)

    for c in range(max_index):
        sum_val += arr[c] if arr[c] > 0 else 0

    return sum_val


def production_of_negatives(arr: list):
    production = 1

    for elem in arr:
        production = production * elem if elem < 0 else production

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

    print("Production of negatives:", production_of_negatives(arr))
    print("Max", lfunc.max(arr), "at", lfunc.max_index(arr))
    print("Sum of positives before max:", sum_of_positives_before_max(arr))
    print("Reversed:", lfunc.reverse(arr))


if __name__ == "__main__":
    main()