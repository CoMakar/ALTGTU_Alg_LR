def is_inside_circle_quarter(x: float, y: float, radius: float):
    if x > 0 and y < 0:
        return False

    return x ** 2 + y ** 2 < radius ** 2


def is_between_circles(x: float, y: float,
                       radius_1: float, radius_2: float):
    if x < 0 and y > 0:
        return False

    point = x ** 2 + y ** 2

    return point > radius_1 ** 2 and point < radius_2 ** 2


def main():
    while True:
        try:
            x = float(input("Enter the x coordinate: ").replace(",", "."))
            y = float(input("Enter the y coordinate: ").replace(",", "."))
            radius_1 = float(input("Enter the Radius_1: ").replace(",", "."))
            radius_2 = float(input("Enter the Radius_2: ").replace(",", "."))
        except ValueError:
            print(" ! Invalid float value")
            continue

        break

    if radius_1 <= 0 or radius_2 <= 0:
        print("Invalid radius value. [radius > 0]")
        return

    if radius_2 <= radius_1:
        print("Radius_2 must be greater than Radius_1")
        return

    point_is_inside_cricle_quarter = is_inside_circle_quarter(x, y, radius_1)
    point_is_between_circles = is_between_circles(x, y, radius_1, radius_2)

    if point_is_inside_cricle_quarter:
        print("Point is inside quarter of the circle")
    elif point_is_between_circles:
        print("Point is between the circles")
    else:
        print("Point does not belong to any area")


if __name__ == "__main__":
    main()