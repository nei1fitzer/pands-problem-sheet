# collatz.py
# This program prompts the user to input a positive integer and generates the Collatz sequence for the given number.
# If the sequence enters an infinite loop, the program will exit with an error message (recursion removed and replaced with loop)
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


def generate_collatz_sequence(num: int) -> None:
    # Generate the Collatz sequence for the given positive integer using a loop.

    step_count = 0
    unique_values = set()

    while num != 1:
        # If the current value has been seen before, exit with an error message
        if num in unique_values:
            print("\nError: Infinite loop detected.")
            sys.exit()
        unique_values.add(num)  # Add the current value to the set of seen values

        # Print the current number in the Collatz sequence
        print(num, end=" ")

        # If the current value is even, divide it by 2; if it's odd, multiply by 3 and add 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

        step_count += 1

    # Print the final number (1) in the Collatz sequence and the total number of steps
    print(num, end=" ")
    print(f"\nNumber of steps: {step_count}")
1
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
