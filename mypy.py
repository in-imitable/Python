# import simplejson as json
# import os

import requests

r = requests.get('https://google.com')
print("Status", r.status_code)

# if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
#     old_file = open("./ages.json", "r+")
#     data = json.loads(old_file.read())
#     print("Current age is", data["age"], "--- adding a year.")
#     data["age"] = data["age"] + 1
#     print("New age is", data["age"])

# else:
#     old_file = open("./ages.json", "w+")
#     data = {"name": "Nick", "age": 27}
#     print("No file found, setting default age to", data["age"])

# old_file.seek(0)
# old_file.write(json.dumps(data))

# newfile = open("newfile.txt", "wr+")

# string = "This is a new file created by python"

# newfile.write(string)
# newfile.read(string)
