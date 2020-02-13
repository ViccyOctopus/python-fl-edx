
#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#The following variables contain values as described below:
#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#For each month, calculate statements on the monthly payment and remaining balance.
#Finally, print out the total amount paid that year and the remaining balance at the end of the year.
#The code you paste into the following box should not specify the values for the variables balance, annualInterestRate, or monthlyPaymentRate - our test code will define those values before testing your submission.

month = 0
totalPay = 0
monthlyInterestRate = annualInterestRate / 12.0
while month <12:
    minPay = monthlyPaymentRate * balance
    unpayBal = balance - minPay
    totalPay += minPay
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
print('Remaining balance: ' + str(round(balance,2)))

#Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#In this problem, we will not be dealing with a minimum monthly payment rate.
#The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.
#Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay.
#The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.

# Loop through to determine minimum fixed payment to pay off in one Year
# Start with $10 payments, increase by $10 each iteration

# Initialize minimum monthly fixed payment
minimumFixedPayment = 0.0

# Copy balance into myBalance
myBalance = balance

# Monthly interest rate
monthlyInterestRate = annualInterestRate/12.0

# Loop through calculating if monthly payment will pay off in 12 months
while myBalance > 0.0:

    # Increment minimum monthly fixed payment by $10 each time through loop
    minimumFixedPayment += 10.0

    # Apply payments and interest for each of twelve months
    # Once balance at end is less then 0 will have
    # calculated min fixed payment
    for month in range (0, 12):

        # Apply payment to balance
        myBalance -= minimumFixedPayment

        # Add interest to balance
        myBalance += (myBalance * monthlyInterestRate)

    if myBalance > 0:
        # Reset balance each time through loop
        myBalance = balance


    # Debugging print statement
    # print "Exited for loop"
    # print "Min payment " + str(round(minimumFixedPayment, 0))


# Print the lowest monthly payment that will pay off the debt in 12 months
print("Lowest Payment " + str(minimumFixedPayment))



# Problem 3 - Using Bisection Search to Make the Program Faster

# (20/20 points)
# You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running
# your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances
# and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission
# is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining
# about too much time taken.)

# Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow
# code?
# We can make this program run faster using a technique introduced in lecture - bisection search!

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What
# is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest,
# the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month.
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we
# ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance
# we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its
# interest compounded monthly for an entire year.

# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find
# the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with
# large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return
# value as you did in Problem 2.

init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))