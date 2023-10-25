import numpy as np
from matplotlib import pyplot as plt


def resolve_y(x: int):
    y = None

    if -7 <= x < -3:
        y = x + 7
    elif -3 <= x < -2:
        y = 4
    elif -2 <= x < 2:
        y = x**2
    elif 2 <= x <= 4:
        y = x * -2 + 8

    return y


def main():
    START = -10
    END = 10
    SAMPLES = 10000
    CONTROL_POINTS = ((-7, 0), (-3, 4), (-2, 4), (0, 0), (2, 4), (4, 0), (4, 0))

    x_data = [i for i in np.linspace(START, END, SAMPLES)]
    y_data = [resolve_y(x) for x in x_data]

    plt.grid(color="k", linewidth=0.5, linestyle=":")
    plt.axvline(x=0, c="black")
    plt.axhline(y=0, c="black")

    plt.plot(x_data, y_data, "b-")
    plt.plot(*zip(*CONTROL_POINTS), "ro")

    plt.xticks(np.arange(-10, 10, step=0.5), rotation=45)
    plt.yticks(np.arange(-10, 10, step=0.5))

    plt.style.use("classic")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
