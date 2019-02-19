print ("This program will help you figure out how long it will take to save up for that sweet house you want")
annual_salary = int(input("Enter your yearly income: "))
portion_saved = float(input("Enter the percent of your salary to save, in decimal: "))
r = (input("Enter the expected annual rate of return [.04]: "))
#if no value is entered the if statement will then run a line to set the value of r to the default value.
if str(r) == "":
    r = 0.04
else:
    r = float(r)
portion_down_payment = (input("Enter the percent of your home's cost to save as a down payment [0.25]: "))
#if no value is entered the if statement will then run a line to set the value of portion_down_payment to the default value.
if str(portion_down_payment) == "":
    portion_down_payment = 0.25;
else:
    portion_down_payment = float(portion_down_payment)
total_cost = int(input("Enter the cost of your dream home: "))

down_payment = total_cost * portion_down_payment
print(down_payment)
current_savings = 0
r = 0.04
#this will take your yearly and turn it to monthly, and figure out how much you save of that amount each month.
portion_saved = annual_salary / 12 * portion_saved
print(portion_saved)

#this will take your savings pool and multiply it by an interest rate to see your monthly return, it then adds that amount to your savings.
current_savings = current_savings + (current_savings / 12 * r)
print(current_savings)

#here we take the monthly portion you are putting into your savings and adding it to your starting monthly amount.
current_savings = portion_saved + current_savings
print(current_savings)

months_needed = 1
running = True
#This loop will run as long as running is valued at True. Once the value of current_savings reaches or exceeds down_payment the loop will end and print out the amount of months needed. 
while running:
   

    if current_savings >= down_payment:
        print ("It will take you ", months_needed," months to put a down payment on your house.")
        running = False
    elif current_savings < down_payment:
        current_savings = current_savings + (current_savings / 12 * r)
        print(current_savings)

        current_savings = portion_saved + current_savings
        print(current_savings)
        months_needed = months_needed + 1 #simple value incrementor. Each time the loop goes through months_needed will increase.
        running = True
