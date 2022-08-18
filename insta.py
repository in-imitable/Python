from instapy_cli import client
from textwrap import dedent

username = 'atulkumar.98'

password = 'ABCD@1234'

img = 'IMG.jpg'

text = dedent("""This picture uploaded with python code on instagram' + 
                '\r\n' + '#pythoncode #programming
    """)

with client(username, password) as cli:
    cli.upload(img, text)
