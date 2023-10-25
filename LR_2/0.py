from math import sin, cos


def main():
    a = float(input("Enter the Alpha number: "))
    
    z1 = 1 - sin(2 * a) / 4 + cos(2 * a)
    z2 = cos(a)**2 + cos(a)**4

    print(f"z1={z1:.8f}; z2={z2:.8f}")


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")