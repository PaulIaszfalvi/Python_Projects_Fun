import json
from colorama import Fore
from urllib.request import urlopen
import ast
import pandas as pd

# Opening JSON file
#f = open("./Basic/people.json")

# with open("./Basic/people.json") as f:
# # returns JSON object as
# # a dictionary
#     data = json.load(f)

# countEmails = 0
# countNoEmails = 0

# for i in data:
#     if i["email"] is not None:
#         print(Fore.BLUE, i["email"])
#         countEmails += 1
#     else:
#         print(Fore.RED, i["name"])
#         countNoEmails +=1 
        
# print("Emails: ", countEmails)
# print("No Emails: ", countNoEmails)
# Closing file
#f.close()

# for state in data:
#     print(state["name"], ", ", state["city"])

with urlopen("https://jsonplaceholder.typicode.com/users") as response:
    source = response.read()

data = json.loads(source)

for s in data:
    print(json.dumps(s, indent=2))
  

#val = data['name'][0]['username'][0]['email']

#pd.DataFrame(val, columns=["time", "temperature", "quality"])