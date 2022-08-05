"""This program will calculate your Life Path number with your birthday."""

name = input('Enter your name: ')

print(f"Hello! {name.title()}.")
print("""This program will calculate your Life Path number with your birthday.
Please enter your Birthday here... Day, Month and Year""")


day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

# birthday = f"{day}\\{month}\\{year}"
# print(birthday)


"""The For Loops are using for adding digits in Day, Month and Year in this program."""
sum_of_day = 0
for i in range(len(str(day))):
    digit = day % 10
    sum_of_day += digit
    day = day // 10


sum_of_month = 0
for i in range(len(str(month))):
    digit = month % 10
    sum_of_month += digit
    month = month // 10


result = 0
for i in range(len(str(year))):
    digit = year % 10
    result += digit
    year = year // 10


sum_of_year = 0
for i in range(len(str(result))):
    digit = result % 10
    sum_of_year += digit
    result = result // 10


master_number = sum_of_day + sum_of_month + sum_of_year


sum_of_master_number = 0
for i in range(len(str(master_number))):
    digit = master_number % 10
    sum_of_master_number += digit
    master_number = master_number // 10
print('Your Life Path number is: ', sum_of_master_number)
