# I imported math to use the math.pow later
import math

# I asked the user to input if he wanted to calculate a bond or investment
# I made the variable "finances" all lowercase so that the user can capitalize in any way they want to
finances = input('''Choose either 'investment' or 'bond' from the menu below to proceed: \n
investment\t - to calculate the amount of interest you'll earn on interest 
bond \t\t - to calculate the amount you'll have to pay on a home loan \n''')
finances = finances.lower()

# I used the condition "while loop" so that the input message will be executed untill the user enters "investment" or "bond"
# If the user did not enter "investment" or "bond" the " Please enter 1 of the 2 given options" message will be displayed and the program will start again
# Again i made sure that the inputed value of the user is in all lowercase
while finances != "investment" and finances != "bond":
    print("Please enter 1 of the 2 given options\n")        # I used line break for readablity
    finances = input('''Choose either 'investment' or 'bond' from the menu below to proceed: \n
investment\t - to calculate the amount of interest you'll earn on interest 
bond \t\t - to calculate the amount you'll have to pay on a home loan \n''')
    finances = finances.lower()

# If the input from the user was "investment" or "bond" the code below will be executed
# The appropriate questions was asked to get the information needed to make the calculation
# The if statement is for when the user inputted "investment" and else is for "bond"
# Again i made sure that the input of the variable "invest" was all lowercase
# Line breaks was used after each question with "\n", so that the format will look better when user types an input
if finances == "investment":
    amount = int(input("What is the amount you are depositing?:\n"))
    percentage = int(input("What is the percentage you are investing at?:\n"))
    number_years = int(input("What is the number of years you are planning on investing for?:\n"))
    interest = input("Do you want simnple or compound interest?:\n")
    interest = interest.lower()
    # I did a while loop statement so that the user can only enter "simple" or "compound"
    # If none if these 2 string are entered it will display "Please enter 1 of the 2 given options" and repeat the question
    # The if statement is for "simple" and else is for "compound"
    # Line breaks was used after each question with "\n", so that the format will look better when user types an input
    while interest != "simple" and interest != "compound":
        print("Please enter 1 of the 2 given options\n")        # I used line break for readablity
        interest = input("Do you want simple or compound interest?:\n")
        interest = interest.lower()
    if interest == "simple":
        interest = amount * (1 + percentage / 100 * number_years)
    else:
        interest = amount * math.pow ((1 + percentage / 100), number_years)
    interest = "{:.2f}".format(interest)        # Formatted for Rand and cent
    print(f"You wil have R {interest} after {number_years} year/'s")

# The appropriate questions was asked to get the information needed to make the calculation
# Line breaks was used after each question with "\n", so that the format will look better when user types an input
else:
    value = int(input("What is the present value of the house?:\n"))
    percentage = int(input("What is the interest rate?:\n"))
    number_months = int(input("What is the amount of months you want to take to repay?:\n"))
    monthly_repayment = (percentage / 100 / 12 * value) / (1 - (1 + percentage) ** (- number_months))
    monthly_repayment = "{:.2f}".format(monthly_repayment)      # Formatted for Rand and cent
    print(f"Your monthly repayment wil be R {monthly_repayment}")

