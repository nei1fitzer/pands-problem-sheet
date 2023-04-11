# bank.py
# This program prompts the user to enter two amounts in cents, adds them together,
# and displays the result in euro.cent format. The user can repeat the program
# multiple times if desired. Negative amounts and non-integer inputs are not allowed.
# author: Neil Fitzgerald
# sources used: Stack Overflow, Python documentation, lecture notes, and ChatGPT for error checking when stuck.

# Infinite loop that asks the user if they wish to re-run the program again. Can only break by inputting 'n' or 'no'. 
continue_program = True
while continue_program:
    # SECTION 1: User is asked to enter first amount in cents.
    try:
        # Input function prompts the user and asks them to enter an amount. The int before this ensures it is an integer value.
        # first_amount is the name given to this variable
        first_amount = int(input("Enter the first amount in cents: "))

        # Error handling, the user cannot enter an amount that is less than 0. If they do they will be prompted with an error message and asked to try again
        # The continue variable makes the loop go back to the beginning and ask the user to input again
        if first_amount < 0:
            print("The first amount cannot be a negative number. Please try again.")
            continue

    # Error handling, if the input is a non-integer value and ValueError is caught, the user will be prompted with an error message and asked to try again
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    # SECTION 2: User is asked to enter second amount in cents
    try:
        # Input function prompts the user and asks them to enter an amount. The int before this ensures it is an integer value.
        # second_amount is the name given to this variable
        second_amount = int(input("Enter the second amount in cents: "))

        # Error handling, the user cannot enter an amount that is less than 0. If they do they will be prompted with an error message and asked to try again
        # The continue variable makes the loop go back to the beginning and ask the user to input again
        if second_amount < 0:
            print("The second amount cannot be a negative number. Please try again.")
            continue

    # Error handling, if the input is a non-integer value and ValueError is caught, the user will be prompted with an error message and asked to try again
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    # Calculate the total amount and display it in euro.cent format
    total_amount = first_amount + second_amount
    print("The total amount is: \u20AC{0:.2f}".format(total_amount/100))


    #SECTION 3: Ask user if they want to repeat the program
    # To break the loop the user will be asked if they want to repeat the process. If they select no the loop breaks. If they select yes they start again.
    while True:
        repeat = input("Do you want to enter more amounts? (y/n): ")

        # If the user enters 'n' or 'no' the loop breaks and the program terminates. The .lower is used to ensure that it can deal with any case input.
        if repeat.lower() in ["n", "no"]:
            print("Goodbye!")
            continue_program = False
            break

        # If the user enters a value other than no/n or yes/y an error message will appear and the loop will continue
        elif repeat.lower() not in ["y", "yes"]:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue

        # If the user enters 'y' or 'yes' the loop breaks and starts again from the beginning.
        else:
            break
