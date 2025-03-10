#even or odd
def check_even_odd():
    #input from the user
    try:
        number = int(input("Please enter an integer: "))

        # Checking if the number is even or odd
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
check_even_odd()