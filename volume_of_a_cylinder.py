def calculate_cylinder_volume(radius, height):
    base_area = 3.142 * radius**2
    volume = base_area * height
    return volume

def main():
    radius = 4
    height = 5
    volume = calculate_cylinder_volume(radius, height)
    print("The volume of the cylinder is:", volume)

# Calling the main function to start the program
main()

