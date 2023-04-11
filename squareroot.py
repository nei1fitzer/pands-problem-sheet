# squareroot.py
# This program computes the square root of a positive number using the Newton-Raphson method.
# This is achieved by creating our own sqrt function and not built in squareroot functions
# author: Neil Fitzgerald
# Sources used: Python documentation, lecture notes, and OpenAI's ChatGPT for error checking when stuck.

def sqrt(n):
    
    # Takes a positive floating-point number as input and returns an approximation of its square root.
    # Newton-Raphson method is used to iteratively refine the estimate until it converges to the square root.
    
    # SECTION 1: Input validation
    # Check if the input number is negative or not a float
    # if number is not int or float ValueError is called
    # if n is equal to 0 it will return 0 (squareroot of 0 is 0)

    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a positive floating-point number")
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    if n == 0:
        return 0

    # SECTION 2: Newton-Raphson method
    # This computres an approxiamte of squareroot of the input 'n'
    # Initialises X to a reasonable starting point (typically 1)
    x = 1

    # Begins an infinite loop that will iteratively refine the estimate of the squareroot using  Newton-Raphson formula
    while True:
        # Calculates the next estimate which is Y using the Newton-Raphson formula: y = (x + n / x) / 2.
        # if the difference between the current and next estimates is smaller than the tolerance value (1e-9)
        # that means the algorithm has found a good enough answer and has converged
        y = (x + n / x) / 2
        if abs(y - x) < 1e-9:
            # Returns the converged value (y) as the final estimate of the square root.
            return y
        # Update the current estimate (x) to the next estimate (y) and repeat the loop.
        x = y


# Main program execution
if __name__ == "__main__":
    # This section will only run if this script is the main program being executed (not imported as a module)

    while True:
        # This is an infinite loop that keeps getting user input and calculating the square root until the user decides to stop

        # SECTION 3: Get input from user and computes squareroot
        
        # Ask the user to input a positive number
        num = input("Enter a positive number: ")

        # Try to convert the user input to a float, in case the input is not a valid number, it will raise a ValueError
        try:
            num = float(num)

            # Call the sqrt function to calculate the square root of the given number and round it to 1 decimal place
            # Result is printed using f string
            print(f"The square root of {num} is approximately {round(sqrt(num), 1)}")

        # If the input is not a valid number ValueError activated and displays below error message
        except ValueError:
            print("Invalid input: Please enter a valid positive number")


        # SECTION 4: Ask user if they wish to run the program again
        answer = input("Do you want to compute another squareroot? (y/n): ")
        if answer.lower() == "n":
            break
