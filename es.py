# es.py
# This program counts the number of 'e's in a plain text file.
# The user provides the file name as a command-line argument
# e.g. if saved in the same folder as the script and the name of the file is Test123, you would type python es.py Test123.txt
# It displays the count of 'e's in the file and asks the user
# if they want to run the program again or exit.
# author: Neil Fitzgerald
# Sources used: Stack Overflow, Python documentation, lecture notes, and OpenAI's ChatGPT for error checking when stuck.

import os
import sys

# Section 1: Function Definitions

# count_e: A function to count the 'e's in a file
def count_e(filename):
    count = 0

    # Open the file in read mode (and close it automatically when done)
    with open(filename, "r") as file:
        # Read the file line by line
        for line in file:
            # Analyze every character within the line
            for char in line:
                # If we've got an 'e' or an 'E', add to the counter
                if char.lower() == "e":
                    count += 1

    # Show the 'e' count and the file's name
    print(f"The file '{filename}' contains {count} e's.")

# ----- Main Program -----

# Check if the user provided a file name as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python es.py <filename>")
    sys.exit(1)

# Take the file name from the command-line argument
filename = sys.argv[1]

# Make sure the file exists and it's a .txt file. It the file is not in the same folder as the script you will need to enter in it's fill path
if not os.path.isfile(filename) or not filename.endswith(".txt"):
    print("Invalid file. Please provide a plain text file (.txt).")
    sys.exit(1)

# Count total e's within the file
count_e(filename)
