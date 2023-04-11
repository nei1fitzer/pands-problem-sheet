# collatz.py
# This program prompts the user to input a positive integer and generates the Collatz sequence for the given number.
# If the sequence enters an infinite loop, the program will exit with an error message.
# author: Neil Fitzgerald
# Sources used: Stack Overflow, Python documentation, lecture notes, and OpenAI's ChatGPT for error checking when stuck.

import sys

def get_positive_integer() -> int:

    #Prompt the user to input a positive integer and validate the input.
    while True:
        try:
            input_num = int(input("Please enter a positive integer: "))
            if input_num > 0:
                return input_num
            else:
                print("Error: The number must be positive.")
        except ValueError:
            print("Error: Invalid input. Please enter a positive integer.")


def generate_collatz_sequence(num: int, step_count: int = 0, unique_values: set = None) -> None:
    #Generate the Collatz sequence for the given positive integer using recursion.
    
    # Initialize the set of unique values on the first call
    if unique_values is None:
        unique_values = set()

    # If the current value has been seen before, exit with an error message
    if num in unique_values:
        print("\nError: Infinite loop detected.")
        sys.exit()
    unique_values.add(num)  # Add the current value to the set of seen values

    # Print the current number in the Collatz sequence
    print(num, end=" ")

    # If the current value is 1, print the total number of steps and return
    if num == 1:
        print(f"\nNumber of steps: {step_count}")
        return

    # If the current value is even, divide it by 2; if it's odd, multiply by 3 and add 1
    if num % 2 == 0:
        next_num = num // 2
    else:
        next_num = num * 3 + 1

    # Recursively call the function with the next number in the sequence
    generate_collatz_sequence(next_num, step_count + 1, unique_values)


while True:
    input_num = get_positive_integer()
    generate_collatz_sequence(input_num)

    # SECTION 4: Ask the user whether they want to run the program again or exit
    while True:
        choice = input("Do you want to run the program again? (Y/N) ").upper()
        if choice == "Y":
            break
        elif choice == "N":
            sys.exit()
        else:
            print("Error: Invalid choice. Please enter Y or N.")
