def is_out_ulcircle(x: float, y: float, radius: float):
    if x > 0 or y < 0:
        return False

    point = (x + radius) ** 2 + (y - radius) ** 2

    return point > radius ** 2 and x > -radius and y < radius


def is_out_brcircle(x: float, y: float, radius: float):
    if x < 0 or y > 0:
        return False

    point = (x - radius) ** 2 + (y + radius) ** 2

    return point > radius ** 2 and x < radius and y > -radius


def main():
    while True:
        try:
            x = float(input("Enter the x coordinate: ").replace(",", "."))
            y = float(input("Enter the y coordinate: ").replace(",", "."))
            radius = float(input("Enter Radius: ").replace(",", "."))
        except ValueError:
            print("Invalid float value")
            continue

        break

    if radius <= 0:
        print("Invalid radius value. [radius > 0]")
        return

    point_is_out_ulcircle = is_out_ulcircle(x, y, radius)
    point_is_out_brcircle = is_out_brcircle(x, y, radius)

    if point_is_out_ulcircle:
        print("Point is out of the upper left circle")
    elif point_is_out_brcircle:
        print("Point is out of the bottom right circle")
    else:
        print("Point does not belong to any area")


if __name__ == "__main__":
    main()