import sys

password = {
    'email': 'eakghfkjiui3urir738iu3rr3yr9',
    'blog': 'jjhoidoh8d39urokenfo83uri3m9',
    'luggage': '123456'
}

if len(sys.argv) < 2:
    print('Usage: py raw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is no account named ' + account)
