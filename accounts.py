# Week 3: 
# Author: Neil Fitzgerald 
# This program prompts the user for an account number and
# masks all but the last 4 digits with Xs. If the account number is not
# 10 digits long, it displays a warning and prompts the user to continue.

while True:
    # Prompt user for account number
    account_number = input("Please enter an account number: ")

    if len(account_number) == 10:
        # If account number is 10 digits long, show 6 xs and last 4 digits
        masked_account_number = "X" * 6 + account_number[-4:]
        print(f"Masked account number: {masked_account_number}")
    else:
        # If account number is not 10 digits long, display warning and prompt user to continue
        print("Warning: Account number is not 10 digits long.")
        response = input("Do you want to continue? (y/n): ")
        if response.lower() not in ("y", "yes"):
            break
        else:
            # Show account number with all but last 4 digits masked with Xs
            masked_account_number = "X" * (len(account_number) - 4) + account_number[-4:]
            print(f"Masked account number: {masked_account_number}")

    # Prompt user to continue
    response = input("Would you like to enter another account number? (y/n): ")
    if response.lower() not in ("y", "yes"):
        break




