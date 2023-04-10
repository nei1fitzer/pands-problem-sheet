#bank.py
#Week 2: This program prompts the user to input two amounts in cents and outputs the answer in euro.cent format. 
#author: Neil Fitzgerald 

# The user is prompted to enter in the first amount (cents)
first_amount = int(input("Enter the first amount in cents: "))

# The user is prompted to enter in the second amount (cents)
second_amount = int(input("Enter the second amount in cents: "))

# Both user input amounts are added together
total_amount = first_amount + second_amount

# The answer is formatted into euro.cent by diving the total amount as an integer '//' (euro) and remainder '%' (cent)
euro = total_amount // 100
cent = total_amount % 100

# This prints the total amount in an easy to read euro.cent format
print("The total amount is: €{}.{:02d}".format(euro, cent))