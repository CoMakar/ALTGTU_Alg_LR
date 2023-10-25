def is_inside_circle(x: int, y: int, radius: int):
    if x >= 0 or y <= 0:
        return False

    circle_equation = x ** 2 + y ** 2

    return circle_equation < radius ** 2


def is_inside_triangle(x: int, y: int, radius: int):
    if y >= 0:
        return False

    if not 0 < x < radius / 2:
        return False

    line_1 = -4 * x
    line_2 = (4 * x) - (radius * 2)

    print(line_1, line_2)

    return y > line_1 and y > line_2


def main():
    x = int(input("X: "))
    y = int(input("Y: "))
    r = int(input("R (Radius): "))

    if r <= 0:
        print("Invalid Radius: ", r)
        return

    inside_cricle = is_inside_circle(x, y, r)
    inside_triangle = is_inside_triangle(x, y, r)

    if inside_cricle:
        print("Point is inside circle")
    elif inside_triangle:
        print("Point is inside triangle")
    else:
        print("Point does not belong to any area")


if __name__ == "__main__":
    main()