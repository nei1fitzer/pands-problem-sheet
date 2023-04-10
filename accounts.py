# accounts.py: 
# This program prompts the user to enter an account number and masks all but the last 4 digits with Xs.
# If the account number is not 10 digits long, it displays a warning and prompts the user to continue.
# author: Neil Fitzgerald
# Sources used: Stack Overflow, Python documentation, lecture notes, and OpenAI's ChatGPT for error checking when stuck.

import sys

# Infinite loop that asks the user if they wish to re-run the program again. Can only break by inputting 'n' or 'no'.
while True:
    # SECTION 1: User is asked to enter an account number.
    # Input function prompts the user and asks them to enter an account number. acc_num is the name given to this variable.
    acc_num = input("Enter account number: ")

    # Check if the account number is exactly 10 digits long.
    if len(acc_num) == 10:
        # If account number is 10 digits long, mask the first 6 digits with Xs and display the last 4 digits.
        # The variable masked_acc_num stores the masked account number as a string.
        masked_acc_num = "X" * 6 + acc_num[-4:]
        print(f"Masked account number: {masked_acc_num}")
    else:
        # If account number is not 10 digits long, display a warning message.
        print("Warning: Account number is not 10 digits long.")
        while True:
            # SECTION 2: Ask the user if they want to continue despite the warning.
            # Input function prompts the user and asks them to enter 'y' or 'n' to continue. user_response is the name given to this variable.
            user_response = input("Do you want to continue? (y/n): ")

            # If the user enters 'n' or 'no', the loop breaks and the program terminates.
            if user_response.lower() in ("n", "no"):
                sys.exit()

            # If the user enters 'y' or 'yes', mask all but the last 4 digits with Xs and display the masked account number.
            # The variable masked_acc_num stores the masked account number as a string.
            elif user_response.lower() in ("y", "yes"):
                masked_acc_num = "X" * (len(acc_num) - 4) + acc_num[-4:]
                print(f"Masked account number: {masked_acc_num}")
                break

            # If the user enters a value other than 'y', 'yes', 'n', or 'no', an error message will appear and the loop will continue
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # SECTION 3: Ask user if they want to enter another account number
    while True:
        # Input function prompts the user and asks them to enter 'y' or 'n' to enter another account number. user_response is the name given to this variable.
        user_response = input("Would you like to enter another account number? (y/n): ")

        # If the user enters 'n' or 'no', the loop breaks and the program terminates.
        if user_response.lower() in ("n", "no"):
            sys.exit()

        # If the user enters 'y' or 'yes', the loop breaks and the program restarts from the beginning.
        elif user_response.lower() in ("y", "yes"):
            break

        # If the user enters a value other than 'y', 'yes', 'n', or 'no', an error message will appear and the loop will continue
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

