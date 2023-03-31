#This programs calculates and displays travel expense
#03/30/2023
#CTI-110 P1HW1 - Travel Expense
#Adriane Cortez
#Get users budget
#Get users desired location
#Get users gas expenses
#Get users accomodation expenses
#Get users food expenses
#Set expenses equal to he sum of gas, accomodations, and food
#Set remaining_balance equal to budget subtract expenses
#Display Location
#Display Budget
#Display fuel expenses
#Display accomodation expenses
#Display food expenses
#Display remaining_balance
 
budget = int(input('Enter Budget: '))
location = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
accomodations = int(input('Approximately, how much will you need for accomadations/hotels? '))
food = int(input('Last, how much do you need for food? '))
expenses = int( gas + accomodations + food)
remaining_balance = int(budget - expenses)

print("------------Travel Expenses------------")
print("Location:            ",location)
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodations:      ${accomodations:.2f}')
print(f'Food:               ${food:.2f}')
print("---------------------------------------") 

print(f'Remaining Balance:  ${remaining_balance:.2f}')
