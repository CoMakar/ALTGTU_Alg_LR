from typing import List


def print_matrix(matrix: List[List], col_width=5, row_sep=" "):
    print("[")
    for row in matrix:
        for element in row:
            print(
                ("    {:<" + str(col_width) + "}").format(
                    "{: }".format(element)
                ),
                end=row_sep,
            )
        print()
    print("]")