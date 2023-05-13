
print('Welcome to the tip calculator.')
bill = input('What was the total bill? $')
people = input('How many people will split the bill?')
percentage = input('What percentage tip would you like to give? 10, 12 or 15?')

operation = round(float(bill) / int(people) * (1 + int(percentage) / 100),1)
print('Each person should pay: %s' %(operation))