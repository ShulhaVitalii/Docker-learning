import calendar

print('Welcome to super calendar\n')

year = int(input('Please enter the year : '))
month = int(input('Please enter the month number : '))

print(calendar.month(year, month))

print('Good luck!')