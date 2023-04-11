# weekday.py
# This program checks if today is a weekday or a weekend.
# author: Neil Fitzgerald
# Sources used: Python documentation, lecture notes, and ChatGPT for error checking when stuck.

import datetime  # Import datetime module to work with dates and times

# SECTION 1: Get today's date using the datetime module
today = datetime.datetime.now().strftime("%A")  # Store the current day of the week as a string

# SECTION 2: Check if today is a weekday (Monday-Friday)
if today == "Saturday" or today == "Sunday":
    print("It is the weekend, yay!")  # If today is Saturday or Sunday, print a message indicating it's the weekend
else:
    # If today is a weekday (Monday-Friday), print a message indicating it's a weekday
    print("Yes, unfortunately today is a weekday.")
