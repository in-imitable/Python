birthdays = {
    'Atul': 'Dec 30',
    'Megha': 'Jun 4',
    'Rishabh': 'May 11'
}

while True:
    print('Enter your name: (blank for quit)')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')

    else:
        print(f"I don't have birthday information for {name}")
        print('What is there birthday?')
        b_day = input()
        birthdays[name] = b_day
        print('Birthday database updated.')
