

# for i in range(5):
#     print(i, end=" ")
# print("\nthis is the end of code")

# display a welcome message
print("Welcome to the Interest rate Calculator") 
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t")) 
    years = int(input("Enter number of years:\t\t")) 


    # check of investment amount is greater than zero
    if monthly_investment > 0:


        # convert yearly values to monthly values 
        monthly_interest_rate = yearly_interest_rate / 12 / 100 
        months = years * 12
        # calculate the future value 
        future_value = 0
        for i in range(months): 
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate 
            future_value += monthly_interest_amount
        # display the result
        print(f"Future value:\t\t\t{round(future_value, 2)}") 
        print()
        # see if the user wants to continue 
        choice = input("Continue (y/n)?: ") 
        print()
    else:
        print(f"Please enter an amount for {monthly_investment} greater than zero")
print("Bye!")





