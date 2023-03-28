Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #This programs calculates and displays travel expense
... #03/28/2023
... #CTI-110 P1HW1 - Travel Expense
... #Adriane Cortez
... #Get users budget
... #Get users desired location
... #Get users gas expenses
... #Get users accomodation expenses
... #Get users food expenses
... #Set expenses equal to he sum of gas, accomodations, and food
... #Set remaining_balance equal to budget subtract expenses
... #Display Location
... #Display Budget
... #Display fuel expenses
... #Display accomodation expenses
... #Display food expenses
... #Display remaining_balance
... 
... budget = int(input('Enter Budget: '))
... location = input('Enter your travel destination: ')
... gas = int(input('How much do you think you will spend on gas? '))
... accomodations = int(input('Approximately, how much will you need for accomadations/hotels? '))
... food = int(input('Last, how much do you need for food? '))
... expenses = int(gas + accomodations + food)
... remaining_balance = int(budget - expenses)
... 
... print("")
... print("------------Travel Expenses------------")
... print("Location: ", location)
... print("Initial Budget: ", budget)
... print("")
... print("Fuel: ", gas)
... print("Accomodation: ", accomodations)
... print("Food: ", food)
... print("")
