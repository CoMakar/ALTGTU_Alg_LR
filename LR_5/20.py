import random as rnd
import lib.list_functions as lfunc


def production_of_positives(arr: list):
    production = 1

    for elem in arr:
        production = production * elem if elem > 0 else production

    return production


def sum_before_min(arr: list):
    sum_val = 0

    min_index = lfunc.min_index(arr)

    for c in range(min_index):
        sum_val += arr[c]

    return sum_val


def separate_even_odd(arr: list):
    evens = []
    odds = []
    for c in range(len(arr)):
        if c % 2 == 0:
            evens.append(arr[c])
        else:
            odds.append(arr[c])

    return evens, odds


def glue_even_odd(evens: list, odds: list):
    len_dif = len(evens) - len(odds)

    if len_dif not in (0, 1):
        raise ValueError("Impossible to glue")

    arr = [0] * len(evens) + [0] * len(odds)

    for c in range(len(arr)):
        if c % 2 == 0:
            arr[c] = evens[c // 2]
        else:
            arr[c] = odds[c // 2]

    return arr


def sort_even_odd(arr: list):
    evens, odds = separate_even_odd(arr)

    evens = lfunc.semi_quick_sort(evens)
    odds = lfunc.semi_quick_sort(odds)

    return glue_even_odd(evens, odds)


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

    print("Production of positives:", production_of_positives(arr))
    print("Min", lfunc.min(arr), "at", lfunc.min_index(arr))
    print("Sum of numbers before min:", sum_before_min(arr))
    print("Odd/Even sorted:", sort_even_odd(arr))


if __name__ == "__main__":
    main()