def is_inside_quarter_circle(x: float, y: float, radius: float):
    if x <= 0 or y <= 0:
        return False
    
    return x ** 2 + y ** 2 < radius ** 2
    
    
def is_inside_triangle(x: float, y: float, radius: float):
    if x >= 0 or y >= 0:
        return False
    
    return y > -x - radius
    

def main():
    while True:
        try:
            x = float(input("Enter the x coordinate (float): ").replace(",", "."))
            y = float(input("Enter the y coordinate (float): ").replace(",", "."))
            radius = float(input("Enter the radius (float): ").replace(",", "."))
        except ValueError:
            print("Invalid floating point number")
        else:
            break
    
    if radius <= 0:
        print("Invalid radius value. [radius > 0]")
        return
    
    point_is_inside_quarter_circle = is_inside_quarter_circle(x, y, radius)
    point_is_inside_triangle = is_inside_triangle(x, y, radius)
    
    print("-"*80)
    
    if point_is_inside_quarter_circle:
        print("Point is inside the quarter of the circle")
    elif point_is_inside_triangle:
        print("Point is inside the triangle")
    else:
        print("Point does not belong to any area :(")
    

if __name__ == '__main__':
    main()