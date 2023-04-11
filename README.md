# Computer Architecture and Technology Convergence

This repository contains a collection of Python programming tasks designed to demonstrate various programming concepts and techniques for the module Computer Architecture and Technology Convergence. Each task is a standalone Python program that can be run independently. The programs cover a range of topics, such as basic input/output, error handling, loops, and plotting.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Task List and Descriptions](#task-list-and-descriptions)
  - [Task01: helloworld.py](#task01-helloworldpy)
  - [Task02: bank.py](#task02-bankpy)
  - [Task03: accounts.py](#task03-accountspy)
  - [Task04: collatz.py](#task04-collatzpy)
  - [Task05: weekday.py](#task05-weekdaypy)
  - [Task06: squareroot.py](#task06-squarerootpy)
  - [Task07: es.py](#task07-espy)
  - [Task08: plottask.py](#task08-plottaskpy)
- [Note on Commits](#note-on-commits)
- [References](#references)

---

## Prerequisites

- **Python 3.6 or higher**

---

## Task List and Descriptions

### Task01: helloworld.py

A simple program that prints "Hello World!" to the console.

**Example output:**

Hello World!

---

### Task02: bank.py

This program prompts the user to enter two amounts in cents, adds them together, and displays the result in euro.cent format. The user can repeat the program multiple times if desired. Negative amounts and non-integer inputs are not allowed.

**Example input and output:**

Enter the first amount in cents: 150
Enter the second amount in cents: 200
The total amount is: €3.50
Do you want to enter more amounts? (y/n): n
Goodbye!

---

### Task03: accounts.py

This program prompts the user to enter an account number and masks all but the last 4 digits with Xs. If the account number is not 10 digits long, it displays a warning and prompts the user to continue.

**Example input and output:**

Enter account number: 1234567890
Masked account number: XXXXXX7890
Would you like to enter another account number? (y/n): n

---

### Task04: collatz.py

A program that prompts the user to enter a positive integer and then applies the Collatz function to the number until it reaches 1. The program prints the sequence and the number of steps taken to reach 1.

**Example input and output:**

Enter a positive integer: 10
10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Number of steps: 6
Do you want to run the program again? (y/n)

---

### Task05: weekday.py

This program checks if today is a weekday or a weekend.

**Example output (Depending if today is weekday or weekend):**

Yes, unfortunately today is a weekday.
It is the weekend, yay!

---

### Task06: squareroot.py

A program that prompts the user to enter a positive number and calculates the square root of the number using the Newton-Raphson method.

**Example output:**
Enter a positive number: 25
The square root of 25.0 is approximately 5.0
Do you want to compute another squareroot? (y/n): n

### Task07: es.py

This program reads a text file and counts the number of occurrences of the letter 'e' (case-insensitive) in the file.

**Example output:**
The letter 'e' occurs 47 times in the file.

### Task08: plottask.py

A Python script that plots a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x) = x^3 in the range [0, 10].

**Requirements:**
matplotlib

**Example output:**
A histogram plot
A plot of the function h(x)=x^3

## Note on Commits

There are fewer commits than expected in this repository due to consolidating work and uploading the files all at once. Future repositories will have more frequent and detailed commit messages to better track changes and progress.

## References

Python Documentation: https://docs.python.org/3/
NumPy Documentation: https://numpy.org/doc/stable/
Matplotlib Documentation: https://matplotlib.org/stable/contents.html
Newton-Raphson Method: https://en.wikipedia.org/wiki/Newton%27s_method
ChatGPT: OpenAI. (2021). GPT-3.5. https://openai.com/blog/gpt-3-5/