print ("This program will help you figure out how long it will take to save up for that sweet house you want")
annual_salary = int(input("Enter your yearly income "))
portion_saved = float(input("Enter the percent of your salary to save, in decimal "))
total_cost = int(input("Enter the cost of your dream home "))

portion_down_payment = total_cost * 0.25
print(portion_down_payment)
current_savings = 0
r = 0.04
portion_saved = annual_salary / 12 * portion_saved
print(portion_saved)


current_savings = current_savings + (current_savings / 12 * r)
print(current_savings)

current_savings = portion_saved + current_savings
print(current_savings)

months_needed = 0
running = True
#This loop will run as long as running is valued at True. Once the value of current_savings reaches or exceeds portion_down_payment the loop will end and print out the amount of months needed. 
while running:
   

    if current_savings >= portion_down_payment:
        print ("It will take you ", months_needed," months to put a down payment on your house.")
        running = False
    elif current_savings < portion_down_payment:
        current_savings = current_savings + (current_savings / 12 * r)
        print(current_savings)

        current_savings = portion_saved + current_savings
        print(current_savings)
        months_needed = months_needed + 1 #simple value incrementor. Each time the loop goes through months_needed will increase.
        running = True