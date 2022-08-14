amount = int(input('Enter amount: '))
currency = input('(D)ollar or (R)upee: ')

if currency.upper() == 'D':
    converted = amount * 72
    print(f"You have Rs {converted}/-")

elif currency.upper() == 'R':
    converted = amount // 72
    print(f"You have $ {converted}/-")

else:
    print("""Please select 'D' or 'R' for currency""")
