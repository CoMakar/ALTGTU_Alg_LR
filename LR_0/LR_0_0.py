def input_int(prompt: str):
    while True:
        user_in = input(prompt)

        if user_in.isdigit():
            user_in = int(user_in)
            break
        else:
            print("Not a valid integer")
        
    return user_in

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
    x = input_int("Specify the X parameter: ")
    y = resolve_y(x)
    
    if y is not None:
        print(f"X:", x, "Y:", y)
    else:
        print(f"Y cannot be resolved for the specified parameter X")
    


if __name__ == "__main__":
    main()
